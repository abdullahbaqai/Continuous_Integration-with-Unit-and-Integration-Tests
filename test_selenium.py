import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# For local development, use webdriver-manager to download compatible ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Comment this line if you want to see the browser

# Always use the executable returned by install() — not the folder
chromedriver_path = ChromeDriverManager().install()
service = Service(executable_path=chromedriver_path)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Test your app
driver.get("http://127.0.0.1:5000")
time.sleep(2)  # Ensure the page loads

heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

print("Test Passed!")

driver.quit()
