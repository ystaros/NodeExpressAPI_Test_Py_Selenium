import pytest
import requests
from selenium import webdriver

from data.users_data import users
from pages.main_page import MainPage

from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

base_url = os.getenv('BASE_URL')
users_endpoint = "/api/users"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.get(base_url)
    yield browser
    browser.quit()
    print("Test completed")


@pytest.fixture(autouse=True)
def delete_users():
    requests.delete(base_url + users_endpoint)


@pytest.fixture()
def create_users():
    for user in users:
        requests.post(base_url + users_endpoint, json=user)


@pytest.fixture(scope="function")
def main_page(browser) -> MainPage:
    return MainPage(browser).open()
