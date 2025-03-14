# Captive-Portal-Auto-Login

Are you tired of the dorm and university captive portal?  
Are you tired of entering your password and username every time you want to connect to the Internet? Don't worry anymore. Captiv-portal-auto-login is at your service.

## What is a Captive Portal?

A captive portal is a web page that is displayed to newly connected users before they are granted broader access to network resources. These portals are commonly used in public Wi-Fi hotspots, campuses, hotels, and dormitories to enforce authentication, payment, or terms of service acceptance before allowing Internet access.

## How It Works

This project automates the login process to a captive portal using Python. The main components include:

- **Selenium WebDriver**: Automates browser interactions to navigate and fill in the login form.
- **Requests**: Checks Internet connectivity by attempting to access a known website (Google) and determining if you're being redirected.
- **Automated Loop**: Periodically checks your connection status and attempts to log in automatically if it detects that you're behind a captive portal.

## Features

- **Automatic Detection**: Periodically checks if you have Internet access.
- **Automated Login**: Automatically fills in and submits your credentials on the captive portal.
- **Headless Operation**: Runs in headless mode using Selenium, so no browser window is required.
- **Easy Configuration**: Simply modify the configuration section to match your portal URL, username, and password.

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [Requests](https://pypi.org/project/requests/)
- Chrome WebDriver (ensure it is installed and in your system's PATH)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Captive-Portal-Auto-Login.git
   cd Captive-Portal-Auto-Login

2. **Install Dependencies:**
   ```bash
   pip install selenium requests

3. **Download Chrome WebDriver:**
   Make sure you have the Chrome WebDriver matching your version of Chrome. Download it from [here](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it’s accessible in your PATH.

## Configuration

Edit the script to update your captive portal details:

- **Portal URL:** Update the `portal_url` variable with your captive portal address. you can find the address when the captive portal opens.
- **Credentials:** Update the `username` and `password` variables with your login details.
- **Customization:** Adjust the time intervals (`time.sleep`) if needed to match your network's response time.



