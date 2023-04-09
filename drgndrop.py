from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
sleep(5)
drg = driver.find_element(By.XPATH, "//*[@id='dropContent']//div[@class='dragableBox' and @id='box5']")
drp = driver.find_element(By.XPATH, "//*[@id='countries']//div[@class='dragableBoxRight' and @id='box105']")
ActionChains(driver).drag_and_drop(drg, drp).perform()
sleep(5)
driver.quit()