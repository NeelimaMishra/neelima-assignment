import builtins
import platform
import time

import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import globals
from constants import duration


class SeleniumOperations(object):
    """Class for selenium operations"""

    default_try = 2

    def __init__(self, create_new_driver_instance=False):
        if create_new_driver_instance:
            builtins.default_driver = self._setup()
        self.driver = default_driver

    def _setup(self):
        """Set up the browser handle"""
        driver = None
        if test_browser == "chrome":
            chromedriver_autoinstaller.install()
            driver_method = "Chrome"
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-extensions")
                options.add_argument(
                    '--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"'
                )
            options.add_argument("window-size=2560,1440")
            driver = getattr(webdriver, driver_method)(options=options)
        elif test_browser == "firefox":
            geckodriver_autoinstaller.install()
            driver_method = "Firefox"
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            options.add_argument("window-size=2560,1440")
            driver = getattr(webdriver, driver_method)(options=options)
        else:
            print(f"Unsupported browser {test_browser}")
        if driver:
            driver.implicitly_wait(20)
        driver.set_page_load_timeout(30)
        return driver

    def maximize_browser_window(self):
        """Maximize browser window size"""
        self.driver.maximize_window()

    def click_element(self, web_element):
        """Click web element"""
        failure = "click_element: too many tries"
        for i in range(0, self.default_try):
            try:
                log.info(f"Clicking element:  {web_element}")
                web_element.click()
                return
            except Exception as error:
                failure = error
                time.sleep(
                    duration.SHORT_WAIT_TIME
                )  # This will eliminate failures due to page load delays

        log.error(f"Failed to click after {self.default_try} tries")
        raise failure

    def send_keys(self, web_element, text, ctrla=False, delay=0):
        """Send keys"""
        if ctrla:
            time.sleep(delay)
            if platform.system().lower() == "darwin":
                web_element.send_keys(Keys.COMMAND + "a")
            else:
                web_element.send_keys(Keys.CONTROL + "a")
            web_element.send_keys(Keys.DELETE)
        web_element.send_keys(text)

    def is_displayed(self, web_element):
        """This method will check is web element displayed"""
        result = web_element.is_displayed()
        return result

    def find_by(self, identifier, locator_strategy="xpath"):
        """Find element by -"""
        strategy = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
        }
        return self.driver.find_element(strategy[locator_strategy], identifier)

    def close_browser(self):
        """This method is to close browser."""
        self.driver.close()

    def quit_browser(self):
        """This method is to quit browser driver."""
        self.driver.quit()

    def open_url(self, url=globals.config_data["URL"]):
        """This method is to quit browser driver."""
        self.driver.get(url)

    def get_current_url(self):
        """This method will get the current web url"""
        return self.driver.current_url

    def hover(self, web_element):
        """Hover over an element"""
        hov = ActionChains(self.driver).move_to_element(web_element)
        hov.perform()

    def hover_and_click(self, web_element):
        self.hover(web_element)
        ActionChains(self.driver).click(web_element).perform()

    def refresh(self):
        """Refresh driver"""
        self.driver.refresh()

    def get_text(self, locator):
        """This method will return the text of a web element"""
        return self.find_by(locator).text

    def send_enter_keys(self, web_element):
        """Send Enter/Return keys"""
        if platform.system().lower() == "darwin":
            web_element.send_keys(Keys.RETURN)
        else:
            web_element.send_keys(Keys.ENTER)

    def find_visible_element(
        self, locator, timeout=duration.DEFAULT_WAIT_TIME
    ):
        """This method will wait for an element to be visible"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        return element

    def is_element_displayed(
        self, locator, timeout=duration.DEFAULT_WAIT_TIME
    ):
        """This method will wait for an element to be visible"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def find_elements_by_xpath(self, locator):
        """Finds elements within the element by xpath"""
        return self.driver.find_elements(By.XPATH, locator)

    def scroll_to_element_and_click(self, web_element):
        """This method scrolls to target element with Actions"""
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element)
        actions.perform()
        actions.click(web_element).perform()

    def find_visible_element_from_list(self, element_list):
        """This method returns the first visible element from the list"""
        for element in element_list:
            if element.is_displayed():
                return element

    def click_in_iframe(self, locator, iframe_locator):
        iframe = WebDriverWait(self.driver, duration.DEFAULT_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, iframe_locator))
        )
        self.driver.switch_to.frame(iframe)
        element = WebDriverWait(self.driver, duration.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()
        # Switch back to the main content after interaction
        self.driver.switch_to.default_content()
