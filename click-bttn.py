from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
assert "The Internet" in driver.title
sleep(3)

element = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
element.send_keys(Keys.LEFT)
sleep(3)    