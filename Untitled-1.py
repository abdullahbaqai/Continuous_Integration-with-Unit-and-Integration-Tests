from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Use Service to specify the ChromeDriver path
service = Service(r"C:\Users\hp\Documents\ci-cd\chromedriver-win32\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
