import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from utils.config import BSTACK_DEMO_URL, DEMO_USERNAME, DEMO_PASSWORD

class TestBStackDemo:
    """Test suite for BrowserStack Demo website"""

    def test_favorite_galaxy_s20_plus(self, driver):
        """
        Test to:
        1. Log into bstackdemo.com
        2. Filter for Samsung devices
        3. Favorite the Galaxy S20+
        4. Verify it's in the favorites page
        """
        # 1. Navigate to BStack Demo site
        driver.get(BSTACK_DEMO_URL)
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shelf-item"))
        )
        
        # Click on Sign In button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin"))
        )
        sign_in_button.click()
        
        # Enter login credentials
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "react-select-2-input"))
        )
        username_field.send_keys(DEMO_USERNAME + Keys.TAB)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "react-select-3-input"))
        )
        password_field.send_keys(DEMO_PASSWORD + Keys.TAB)
        
        # Click on Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-btn"))
        )
        login_button.click()
        
        # Wait for the username to be visible, indicating successful login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "username"))
        )
        
        # 2. Filter for Samsung devices
        # Click on the vendor filter for Samsung
        # First confirm it's present
        samsung_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox'][value='Samsung']"))
        )

        # Then force-click it via JavaScript (if needed)
        driver.execute_script("arguments[0].click();", samsung_filter)
        
        # Wait for the filter to apply
        time.sleep(2)  # Adding a small delay to ensure filter is applied
        
        # 3. Find and favorite the Galaxy S20+
        # First locate the product
        galaxy_s20_plus_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Galaxy S20+')]/ancestor::div[contains(@class, 'shelf-item')]"))
        )
        
        # Click the favorite heart icon
        favorite_icon = galaxy_s20_plus_item.find_element(By.XPATH, ".//div[contains(@class, 'shelf-stopper')]/button")
        favorite_icon.click()
        
        # Wait for the favorite action to complete
        time.sleep(1)
        
        # 4. Go to the Favorites page
        favorites_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "favourites"))
        )
        favorites_link.click()
        
        # Wait for the favorites page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shelf-container"))
        )
        
        # Verify that Galaxy S20+ is in the favorites list
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Galaxy S20+')]"))
            )
            # If found, test passes
            assert True
        except:
            # If not found, test fails
            assert False, "Galaxy S20+ was not found in the favorites page"