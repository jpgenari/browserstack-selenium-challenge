import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# BrowserStack credentials - fetch from environment variables
BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME')
BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY')

# Demo site credentials
DEMO_USERNAME = os.getenv('DEMO_USERNAME', 'demouser')
DEMO_PASSWORD = os.getenv('DEMO_PASSWORD', 'testingisfun99')

# BrowserStack capabilities for different browsers
BROWSERS = {
    'windows_chrome': {
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '10',
        'sessionName': 'Windows Chrome Test'
    },
    'mac_firefox': {
        'browserName': 'Firefox',
        'browserVersion': 'latest',
        'os': 'OS X',
        'osVersion': 'Ventura',
        'sessionName': 'macOS Firefox Test'
    },
    'galaxy_s22': {
        'deviceName': 'Samsung Galaxy S22',
        'platformName': 'Android',
        'platformVersion': '12.0',
        'sessionName': 'Samsung Galaxy S22 Test',
        'realMobile': 'true'
    }
}

# BrowserStack Hub URL
BROWSERSTACK_HUB_URL = (
    f'https://{BROWSERSTACK_USERNAME}:'
    f'{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'
)

# Test site URL
BSTACK_DEMO_URL = 'https://www.bstackdemo.com'
