from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("selenium automation")
search_box.submit()
time.sleep(5)
driver.quit()
