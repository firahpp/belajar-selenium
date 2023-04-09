from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from assertpy import assert_that

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")
assert "The Internet" in driver.title #mastiin "The Internet" ada di dalam judul

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
btn_login = driver.find_element(By.XPATH, "//button[@type='submit']")

#negative case
username.send_keys("firah")         
password.send_keys("firaah@")
btn_login.click()

flash_error = driver.find_element(By.XPATH, "//div[@id='flash']")
assert_that(flash_error.text).contains("Your username is invalid!")

#positive case
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
btn_login = driver.find_element(By.XPATH, "//button[@type='submit']")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
btn_login.click()

flash_error = driver.find_element(By.XPATH, "//div[@id='flash']")
assert_that(flash_error.text).contains("You logged into a secure area!") 
sleep(3)