from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium import webdriver

# Configuration
portal_url = "http://10.12.16.1:8002/index.php?zone=cpzone"  # The Captive portal URL
username = "your_username"  # Replace with your username
password = "your_password"  # Replace with your password


def setup_driver():
    """
    Set up Selenium WebDriver with headless options.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def is_internet_connected():
    """
    Check if the internet is connected by detecting redirections to a captive portal.
    """
    try:
        response = requests.get("http://www.google.com", timeout=5, allow_redirects=False)

        # Check if we are being redirected (common for captive portals)
        if response.status_code in [301, 302] or "Location" in response.headers:
            print("Redirect detected! Likely a captive portal.")
            return False

        # Check for unexpected HTML content (e.g., captive portal page instead of Google's page)
        if "google" not in response.text.lower():
            print("Unexpected response content! Likely a captive portal.")
            return False

        # If no redirects and content is valid, internet is connected
        return True

    except (requests.ConnectionError, requests.Timeout) as e:
        print(f"Connection error: {e}")
        return False


def login_to_portal(driver):
    """
    Automate the login process using Selenium.
    """
    try:
        # Open the portal login page
        driver.get(portal_url)

        # Wait for the page to load
        time.sleep(10)

        # Find username and password fields and input the credentials
        username_field = driver.find_element(By.ID, "auth_user")
        password_field = driver.find_element(By.ID, "auth_pass")

        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete
        time.sleep(2)

        print("Login attempt complete.")
    except Exception as e:
        print(f"Error during login: {e}")


# Main loop
if __name__ == "__main__":
    # driver = setup_driver()
    while True:
        try:
            if not is_internet_connected():
                print("No internet connection. Attempting to log in...")
                driver = setup_driver()
                time.sleep(5)
                login_to_portal(driver)
            # else:
                # print("Internet is connected.")

            time.sleep(70)
        except:
            driver.quit()
