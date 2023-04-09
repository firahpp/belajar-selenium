from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")
assert "The Internet" in driver.title
sleep(3)
element = driver.find_element(By.XPATH, "//input[@type='number']")
element.clear()
element.send_keys("1234567890")
element.send_keys(Keys.RETURN)