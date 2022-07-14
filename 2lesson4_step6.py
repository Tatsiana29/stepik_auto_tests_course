from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)

    browser.get(link)

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()

