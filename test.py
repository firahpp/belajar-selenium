from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
assert "Google" in driver.title #test untuk memastikan ada kata 'python' di judul ASSERT = TRUE
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("Firah Putri Pratiwi") 
sleep(3)
elem.send_keys(Keys.RETURN)


#assert "No results found." not in driver.page_source
driver.close()