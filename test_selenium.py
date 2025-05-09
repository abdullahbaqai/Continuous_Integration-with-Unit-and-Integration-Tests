import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Keep this for CI use

# Automatically download the correct ChromeDriver version
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Run your test
driver.get("http://127.0.0.1:5000")
time.sleep(2)

heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text
print("Test Passed!")

driver.quit()
