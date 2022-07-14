from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()