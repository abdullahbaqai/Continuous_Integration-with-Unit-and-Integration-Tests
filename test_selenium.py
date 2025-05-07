from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options for headless CI environments
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Required for CI environments
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.binary_location = "/usr/bin/google-chrome"  # Point to correct Chrome binary

# Create WebDriver instance with configured options
driver = webdriver.Chrome(options=options)

# Open your local Flask app
driver.get("http://127.0.0.1:5000")

# Wait to let the page load
time.sleep(2)

# Check if the expected heading exists
heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

print("Test Passed!")

driver.quit()
