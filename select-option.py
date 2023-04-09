from selenium.webdriver.support.ui import Select
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/dropdown")
assert "The Internet" in driver.title
sleep(3)
select = Select(driver.find_element(By.XPATH, "(//select[@id='dropdown'])[1]"))
select.select_by_visible_text("Option 1")
select.select_by_value(1)
sleep(3)