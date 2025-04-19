import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.get("https://nodeexpressapi-39yx.onrender.com")
    yield browser
    browser.quit()
    print("Test completed")