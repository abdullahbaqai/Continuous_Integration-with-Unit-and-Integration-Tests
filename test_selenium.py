import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options for headless CI environments
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use environment variable for Chromium binary location (set in CI)
options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")

# Automatically install matching ChromeDriver
service = Service(ChromeDriverManager().install())

# Create WebDriver instance with configured options and service
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Flask app and run test
    driver.get("http://127.0.0.1:5000")
    time.sleep(2)
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert "Welcome to Flask!" in heading.text
    print("Test Passed!")
finally:
    driver.quit()
