import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://volejbols.lv"
driver.get(url)

time.sleep(2)

find=driver.find_element(By.CLASS_NAME, "js_acceptCookiePolicy")
find.click()

find=driver.find_element(By.CLASS_NAME, "calendarWrapper")
find.click()

time.sleep(15)

find=driver.find_elements(By.CLASS_NAME, "navItemWrapper")[1]
find.click()

find=driver.find_element(By.CLASS_NAME, "submenuItem")
find.click()

time.sleep(1)

find=driver.find_element(By.LINK_TEXT, "SPĒLĒTĀJI")
find.click()

input()