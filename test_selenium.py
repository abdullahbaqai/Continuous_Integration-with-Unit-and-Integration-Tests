import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Run Chrome in headless mode (Uncomment for CI environments)

# Determine the environment (CI or local) and set up the appropriate ChromeDriver path
if os.getenv("GITHUB_ACTIONS"):
    # In CI, use the pre-installed driver path for Linux (if applicable)
    service = Service("/usr/bin/chromedriver")
else:
    # Locally, use `webdriver-manager` to automatically download the correct driver
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())

# Start Chrome browser with the configured options
driver = webdriver.Chrome(service=service, options=options)

# Test logic: Navigate to your Flask app running locally
driver.get("http://127.0.0.1:5000")
time.sleep(2)  # Wait for the page to load

# Validate that the heading contains the expected text
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

print("Test Passed!")

# Close the browser after the test is complete
driver.quit()
