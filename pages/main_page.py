from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    class Locator:
        SEARCH_TAB = (By.LINK_TEXT, "Search")

    def __init__(self, browser, timeout=5):
        super().__init__(browser, timeout=timeout)
        self.url = self.base_url + "/"

    def go_to_search_page(self):
        from pages.search_page import SearchPage
        self.wait_to_be_clickable(self.Locator.SEARCH_TAB).click()
        return SearchPage(self.browser).wait_for_url()
