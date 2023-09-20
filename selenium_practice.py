from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org")
time.sleep(2)
events = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
events_list = events.find_elements(By.TAG_NAME,'li')
# events_dict = {}
# i = 0
# for event in events_list:
#     day, name = event.text.split('\n')
#     events_dict[i] = {'time':day, "name":name}
#     i+=1
events_dict={}
for i in range(len(events_list)):
    day, name = events_list[i].text.split('\n')
    events_dict[i] ={
        "time" : day,
        "name" : name
    }

print(events_dict)

driver.quit()