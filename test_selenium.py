import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/google-chrome")

# Use system-installed ChromeDriver
service = Service("/usr/bin/chromedriver")

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Test logic
driver.get("http://127.0.0.1:5000")
time.sleep(2)
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text
print("Test Passed!")
driver.quit()
