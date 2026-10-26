import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors") # to ignore SSl certificate

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scroll(0, document.body.scrollHeight)")
driver.get_screenshot_as_file("screenshot.png")

time.sleep(2)