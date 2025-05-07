from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # or specify path to chromedriver

# Open your local Flask app
driver.get("http://127.0.0.1:5000")

# Wait to let the page load
time.sleep(2)

# Check if the expected heading exists
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

print("Test Passed!")

driver.quit()
