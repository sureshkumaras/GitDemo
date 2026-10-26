import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))
for checkbox in checkboxes:
    print(checkbox.text)
    if checkbox.get_attribute("value") == "option2" :
        checkbox.click()
        assert  checkbox.is_selected() ==True
        print(checkbox.is_selected())
        break
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
alert.dismiss()


time.sleep(5)