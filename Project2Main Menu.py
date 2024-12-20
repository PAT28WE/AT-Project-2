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
# List of expected modules to verify
modules = [
    "Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", 
    "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"
]

# Wait for each module and verify its visibility
for module in modules:
    try:
        # Construct XPath for the module
        module_xpath = f"//span[text()='{module}']"  # Assuming the module names are wrapped in <span> elements
        
        # Wait for the module to be visible
        module_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, module_xpath)))
        
        # Print the status if the module is visible
        print(f"{module} module is displayed.")
    except TimeoutException:
        print(f"Error: {module} module is not displayed within the timeout period.")
