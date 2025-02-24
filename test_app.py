from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up ChromeDriver service (Make sure chromedriver.exe is in your project folder)
service = Service("C:/Users/HP/ci-cd-demo/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get("file:///C:/Users/HP/ci-cd-demo/index.html")  # Use your correct file path

# Find element and check text
heading = driver.find_element(By.ID, "greeting")
assert heading.text == "Hello, World!"

# Close the browser
driver.quit()
