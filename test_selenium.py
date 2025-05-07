import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options and service
options = Options()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Test logic
driver.get("http://127.0.0.1:5000")
time.sleep(2)  # Wait for 2 seconds to allow the page to load

# Locate the heading and check its text
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

# Print success message and quit the driver
print("Test Passed!")
driver.quit()
