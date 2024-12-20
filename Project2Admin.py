from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# Full path to the WebDriver executable
driver_path = "C:/Users/HP/OneDrive/Desktop/driver/chromedriver-win64/chromedriver.exe"  # Update this if needed
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")  # Replace with the actual URL

# Wait for the username field to be visible and interact with it
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
username_field.send_keys("Admin")  # Replace with the actual username
print("Entered the username successfully.")

# Wait for the password field to be visible and interact with it
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("admin123")  # Replace with the actual password
print("Entered the password successfully.")

# Wait for the login button to be clickable and then click it
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))
    )
    driver.execute_script("arguments[0].click();", login_button)  # Click using JavaScript if standard click doesn't work
    print("Login button clicked successfully.")
except TimeoutException:
    print("Error: The login button is not clickable within the timeout period.")

# Wait for the Admin module to be visible and clickable
try:
    admin_module = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))  # XPath for Admin module
    )
    admin_module.click()
    print("Admin module clicked successfully.")
except TimeoutException:
    print("Error: Admin module is not clickable within the timeout period.")
screenshot_path = "C:/Users/Ramesh-D7/Desktop/admin_module_screenshot.png"  # Change the path as needed
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved at {screenshot_path}")

# Wait for the Admin page to load (adjust wait time based on your page load)
time.sleep(10)  # You can replace this with an explicit wait for a specific element on the Admin page