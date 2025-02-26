from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use ChromeDriver without specifying a path
service = Service()  
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/login")

# Perform login test...


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
