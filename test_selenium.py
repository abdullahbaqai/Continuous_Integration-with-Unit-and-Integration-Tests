from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/usr/bin/chromium-browser"  # or "/usr/bin/chromium"

driver = webdriver.Chrome(options=chrome_options)
