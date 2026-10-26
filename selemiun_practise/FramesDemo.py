import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
message = driver.find_element(By.ID, "tinymce").text
print(message)

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)

