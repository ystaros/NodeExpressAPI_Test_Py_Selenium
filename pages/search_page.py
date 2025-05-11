from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    class Locator:
        LAST_NAME_FIELD = (By.ID, "lastName")
        SEARCH_BUTTON = (By.ID, "searchButton")
        TDS = (By.CSS_SELECTOR, "tbody>tr>td")

    def __init__(self, browser, timeout=5):
        super().__init__(browser, timeout=timeout)
        self.url = self.base_url + "/search"

    def type_last_name(self, last_name):
        self.wait_to_be_visible(self.Locator.LAST_NAME_FIELD).send_keys(last_name)
        return self

    def click_search(self):
        self.wait_to_be_clickable(self.Locator.SEARCH_BUTTON).click()
        return self

    def get_last_name_td_text(self):
        return self.wait_to_be_visible_all(self.Locator.TDS)[1].text
