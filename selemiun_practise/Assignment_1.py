import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
##########################
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windows = driver.window_handles
driver.switch_to.window(windows[1]) 

getText = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
text = getText.split("at")
actualText = text[1].split("with")
email = actualText[0].strip()
print(email)

driver.close()
driver.switch_to.window(windows[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
message = wait.until(expected_conditions.visibility_of_element_located( (By.XPATH, "//div[@class='alert alert-danger col-md-12']"))).text

print(message)
