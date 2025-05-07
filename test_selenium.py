from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass the sandbox for CI environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
chrome_options.add_argument("--remote-debugging-port=9222")  # Use remote debugging port
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (if needed)

driver = webdriver.Chrome(options=chrome_options)
