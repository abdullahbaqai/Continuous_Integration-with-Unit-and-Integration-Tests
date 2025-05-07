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

# Automatically download and set up the appropriate chromedriver version
service = Service(ChromeDriverManager().install())  # Automatically uses the correct version
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
