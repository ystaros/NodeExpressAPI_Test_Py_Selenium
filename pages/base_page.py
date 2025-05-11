from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment


class BasePage:
    def __init__(self, browser: WebDriver, timeout = 5):
        self.base_url = os.getenv('BASE_URL')
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout=timeout)
        # self.logger = logging.getLogger(self.__class__.__name__)

    def open(self):
        self.browser.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        try:
            WebDriverWait(self.browser, 60).until(EC.url_to_be(self.url))
        except TimeoutException:
            print(f"Timeout when waiting for url {self.url}, current url: {self.browser.current_url}")
        return self

    def find_element(self, by, selector):
        return self.browser.find_element(by, selector)

    def find_elements(self, by, selector):
        return self.browser.find_elements(by, selector)

    def _wait_for(self, locator, condition, timeout):
        return WebDriverWait(self.browser, timeout).until(condition(locator))

    def wait_for_element(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.presence_of_element_located, timeout)

    def wait_to_be_clickable(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.element_to_be_clickable, timeout)

    def wait_to_be_visible(self, locator, timeout = 5) -> WebElement:
        return self._wait_for(locator, EC.visibility_of_element_located, timeout)

    def wait_to_be_visible_all(self, locator, timeout = 5) ->  list[WebElement]:
        return self._wait_for(locator, EC.visibility_of_all_elements_located, timeout)

    def wait_text_to_be_present(self, locator, text, timeout = 5) -> bool:
        return WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))

