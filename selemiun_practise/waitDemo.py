import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
##########################
driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4) # -> exceptional for this condition
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
assert len(results) > 0

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(4)
promocode = "rahulshettyacademy"
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys(promocode)
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
#time.sleep(6)
message = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(message)

time.sleep(20)
