import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("give the lo cation of the downloaded driver ///chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)

time.sleep(5)