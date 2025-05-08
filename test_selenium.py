import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Ensure Chrome runs headlessly
options.add_argument('--remote-debugging-port=9222')  # Add remote debugging port

# Use webdriver-manager to install the correct version of ChromeDriver
service = Service(ChromeDriverManager().install())

# Start Chrome browser
driver = webdriver.Chrome(service=service, options=options)

try:
    # Test logic
    driver.get("http://127.0.0.1:5000")

    # Wait until the heading is present (or any other condition that ensures page has loaded)
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # Validate heading
    assert "Welcome to Flask!" in heading.text

    print("Test Passed!")

finally:
    # Ensure driver quits even if an error occurs
    driver.quit()
