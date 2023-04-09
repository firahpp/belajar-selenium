from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
assert "The Internet" in driver.title
sleep(3)

source = driver.find_element(By.XPATH, "//div[@id='column-a']")
target = driver.find_element(By.XPATH, "//div[@id='column-b']")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()

driver.close()