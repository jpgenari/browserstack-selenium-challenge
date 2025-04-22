import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.config import BROWSERSTACK_HUB_URL, BROWSERS

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="windows_chrome",
                    help="Browser configuration to use for testing")

@pytest.fixture
def browser_config(request):
    return BROWSERS[request.config.getoption("--browser")]

@pytest.fixture
def driver(browser_config):
    """
    Initialize WebDriver based on the browser configuration
    """
    browser_name = browser_config.get('browserName', '')
    
    capabilities = {
        'bstack:options': {
            'userName': BROWSERSTACK_HUB_URL.split('//')[1].split(':')[0],
            'accessKey': BROWSERSTACK_HUB_URL.split(':')[2].split('@')[0],
            'sessionName': browser_config.get('sessionName', 'BStack Demo Test'),
        }
    }
    
    # Add browser-specific capabilities
    if 'deviceName' in browser_config:
        # Mobile configuration
        capabilities['bstack:options'].update({
            'deviceName': browser_config['deviceName'],
            'platformName': browser_config['platformName'],
            'platformVersion': browser_config['platformVersion'],
            'realMobile': browser_config.get('realMobile', 'false')
        })
    else:
        # Desktop configuration
        capabilities['bstack:options'].update({
            'os': browser_config['os'],
            'osVersion': browser_config['osVersion'],
        })
        capabilities.update({
            'browserName': browser_config['browserName'],
            'browserVersion': browser_config['browserVersion'],
        })
    
    # Initialize the appropriate driver
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_HUB_URL,
        desired_capabilities=capabilities
    )
    
    # Set window size for desktop browsers
    if 'deviceName' not in browser_config:
        driver.set_window_size(1366, 768)
    
    # Yield the driver for the test
    yield driver
    
    # Quit the driver after the test
    driver.quit()

