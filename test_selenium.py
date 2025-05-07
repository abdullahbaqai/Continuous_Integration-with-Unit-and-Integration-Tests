import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use environment variable
options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

# Run test
driver.get("http://127.0.0.1:5000")
time.sleep(2)
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text
print("Test Passed!")
driver.quit()
