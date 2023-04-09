from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from assertpy import assert_that

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")
assert "The Internet" in driver.title #mastiin "The Internet" ada di dalam judul

angka = "777"
element = driver.find_element(By.XPATH, "//input[@type='number']")
element.clear()
element.send_keys(angka)
sleep(3)
print("Value of input box: " + element.get_attribute('value'))

assert_that(element.get_attribute('value')).is_equal_to(angka)  #test untuk mastiin value 
#assert "456" in element.get_attribute('value')