from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')
time.sleep(3)
driver.find_element(By.ID, "login").click()
driver.find_element(By.ID, "email").send_keys('maneesha@gmail.com')
time.sleep(1)
driver.find_element(By.ID, "password").send_keys('12345678')
time.sleep(1)
driver.find_element(By.ID, "log").click()
time.sleep(1)
alert = Alert(driver)
alert.accept()
driver.find_element(By.ID, "city").send_keys('Bapatla')
time.sleep(2)
driver.find_element(By.ID, "find").click()
time.sleep(5)
driver.find_element(By.ID, "home").click()
time.sleep(1)
driver.find_element(By.ID, "out").click()
time.sleep(4)
driver.close()