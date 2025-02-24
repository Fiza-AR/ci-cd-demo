from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up headless mode for CI/CD
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")  # Required for CI/CD
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues

# Use the correct path for ChromeDriver in GitHub Actions
service = Service("/usr/local/bin/chromedriver")  # Ubuntu default path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the web page
driver.get("file:///home/runner/work/ci-cd-demo/ci-cd-demo/index.html")  # Update path if needed

# Find element and check text
heading = driver.find_element(By.ID, "greeting")
assert heading.text == "Hello, World!"

# Close the browser
driver.quit()
