from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
