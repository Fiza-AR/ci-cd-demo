from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set ChromeDriver path
chrome_driver_path = r"C:\Users\HP\ci-cd-demo\drivers\chromedriver.exe"

# Set up Chrome options
chrome_options = Options()
# Comment out headless mode if you want to see the browser
# chrome_options.add_argument("--headless")

# Start WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open login page
driver.get("https://the-internet.herokuapp.com/login")

# Wait until username field is present
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))

# Enter login details
username_field.send_keys("tomsmith")  # Standard user
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for success message
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "flash.success")))

# Print success message
print("Login successful!")

# Close the browser
driver.quit()
