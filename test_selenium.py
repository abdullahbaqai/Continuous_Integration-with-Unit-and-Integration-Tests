import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Explicitly set CHROME_BIN if needed (useful in CI)
chrome_path = os.getenv("CHROME_BIN", "/usr/bin/google-chrome")
options.binary_location = chrome_path

# Use correct binary path from ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Run test
driver.get("http://127.0.0.1:5000")
time.sleep(2)
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text
print("Test Passed!")
driver.quit()
