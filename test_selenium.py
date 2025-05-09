from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Force version match if necessary:
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(version="124.0.6367.91").install()),
    options=options
)


# Test your app
driver.get("http://127.0.0.1:5000")
time.sleep(2)  # Ensure the page loads

heading = driver.find_element(By.TAG_NAME, "h1")
assert "Welcome to Flask!" in heading.text

print("Test Passed!")

driver.quit()
