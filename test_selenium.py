from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_homepage():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for CI
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("http://localhost:5000")
    time.sleep(2)  # Wait for server to load
    
    assert "Welcome to MyApp" in driver.page_source
    driver.quit()
