from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import Keys to use it
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

try:
    # Ensure the page is fully loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Wait for the Forgot Password text to be visible
    forgot_password = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))
    )
    
    # Use JavaScript click if standard click doesn't work
    driver.execute_script("arguments[0].click();", forgot_password)
    print("Forgot password clicked successfully.")
    
except TimeoutException:
    print("Error: The Forgot Password link is not clickable within the timeout period.")
    driver.save_screenshot('screenshot_before_click.png')

try:
    # Wait for the username input field to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    
    # Enter the username
    username_field.send_keys("demo_user")  # Replace with the actual username
    print("Username entered successfully.")
    
except TimeoutException:
    print("Error: The username field is not visible or interactable within the timeout period.")

try:
    # Wait for the Reset Password button to be clickable
    reset_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']"))
    )
    
    # Click the Reset Password button
    reset_password_button.click()
    print("Reset Password button clicked successfully.")
    
except TimeoutException:
    print("Error: The Reset Password button is not clickable within the timeout period.")

print("Holding the screen for 1 minute. Do not close the browser manually.")
time.sleep(60)  # Wait for 60 seconds (1 minute)