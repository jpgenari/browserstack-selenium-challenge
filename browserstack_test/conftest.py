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
    is_mobile = 'deviceName' in browser_config

    bstack_options = {
        'userName': BROWSERSTACK_HUB_URL.split('//')[1].split(':')[0],
        'accessKey': BROWSERSTACK_HUB_URL.split(':')[2].split('@')[0],
        'sessionName': browser_config.get('sessionName', 'BStack Demo Test'),
    }

    if is_mobile:
        # Mobile-specific capabilities
        bstack_options.update({
            'deviceName': browser_config['deviceName'],
            'platformName': browser_config['platformName'],
            'platformVersion': browser_config['platformVersion'],
            'realMobile': browser_config.get('realMobile', 'false'),
        })
        # Mobile: Use minimal ChromeOptions
        options = ChromeOptions()
        options.set_capability('bstack:options', bstack_options)
    else:
        # Desktop-specific capabilities
        bstack_options.update({
            'os': browser_config['os'],
            'osVersion': browser_config['osVersion'],
        })
        browser_name = browser_config['browserName']
        browser_version = browser_config['browserVersion']

        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        options.set_capability('browserName', browser_name)
        options.set_capability('browserVersion', browser_version)
        options.set_capability('bstack:options', bstack_options)

    # Init driver
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_HUB_URL,
        options=options
    )

    if not is_mobile:
        driver.set_window_size(1366, 768)

    yield driver
    driver.quit()
