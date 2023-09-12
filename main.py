import requests
from datetime import datetime
import time
import smtplib

def send_email():
    my_email = '-'
    my_text = f"Subject:Quote\n\nThis is time to look at the sky for ISS"

    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls() # make safe connection

        connection.login(my_email,'-')

        connection.sendmail(from_addr=my_email, to_addrs='-',msg=my_text)

MY_LAT = 37.541093
MY_LONG = 126.980588

parameter = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}



def is_on_up():
    response_ISS = requests.get(url="http://api.open-notify.org/iss-now.json")
    # 모든 상황을 조건문으로 만들 필요없이 에러 발생시 해당 이유를 출력해주는 함수 
    response_ISS.raise_for_status() 
    longitude = float(response_ISS.json()["iss_position"]["longitude"])
    latitude = float(response_ISS.json()["iss_position"]["latitude"])
    if abs(longitude - MY_LONG) >5 or abs(latitude - MY_LAT) >5: return False
    return True
    
def is_dark():    
    today = datetime.now()
    time_now = today.hour
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunrset = int(data["results"]["sunrset"].split('T')[1].split(':')[0])
    if time_now >= sunrset or time_now <= sunrise:
        return True
    return False
   
operate = True
while operate:
    time.sleep(60)
    if is_on_up() and is_dark():
        send_email()
        operate  = False
        


# # 1XX : Hold on         가다려라
# # 2XX : Here You GO     완료
# # 3XX : Go Away         권한이 없으니 가라
# # 4XX : You Screwed Up  여러분이 잘못되었다
# # 5XX : I Screwed Up    내가(서버가) 잘못되었다






# 1. if the iss is close to my_current_position 
# and it is currently dark, send me an email to tell me to look up.
