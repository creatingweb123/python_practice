import smtplib
import datetime as dt
import pandas as pd
import random
##################### Extra Hard Starting Project ######################



# should be between 1-3
def make_letter_path():
    letter_number = random.randint(1,3)
    letter_path = f'/Users/user/OneDrive/바탕 화면/language/python 학습자료/birthday-wisher-extrahard-start/letter_templates/letter_{letter_number}.txt'
    return letter_path

def send_birthday_email(maden_letter,send_email):
    my_email = 'shegegegey1@gmail.com'
    my_text = f"Subject:Quote\n\n{maden_letter}"

    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls() # make safe connection

        connection.login(my_email,'moeujpfulglyfajq')

        connection.sendmail(from_addr=my_email, to_addrs=send_email,msg=my_text)


data = pd.read_csv("/Users/user/OneDrive/바탕 화면/language/python 학습자료/birthday-wisher-extrahard-start/birthdays.csv")

birthday_data_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

now = dt.datetime.now()
today_tuple = (now.month, now.day)


if today_tuple in birthday_data_dict:
    letter_path = make_letter_path()
    birthday_person = birthday_data_dict[today_tuple]
    name = birthday_person['name']
    email = birthday_person['email']
    with open(letter_path, 'r') as file:
            #
            contents = file.read()
            contents = contents.replace("[NAME]",name)
    send_birthday_email(contents,email)

