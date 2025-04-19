from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait5(browser, locator):
    waiter = WebDriverWait(browser, 5)
    return waiter.until(EC.visibility_of_element_located(locator))

def wait_all_5(browser, locator):
    waiter = WebDriverWait(browser, 5)
    return waiter.until(EC.visibility_of_all_elements_located(locator))

def test_open_url(browser):
    h1_text = wait5(browser, (By.CSS_SELECTOR, "h1")).text


    assert browser.title == "Users App"
    assert h1_text == "Node Express API Server App."

def test_add_button(browser):
    add_btn = browser.find_element(By.ID, "addButton")

    assert not add_btn.is_enabled() & add_btn.is_displayed()

def test_add_user(browser):
    add_btn = browser.find_element(By.ID, "addButton")

    browser.find_element(By.ID, "firstName").send_keys("Lena")
    browser.find_element(By.ID, "lastName").send_keys("Petrova")
    browser.find_element(By.ID, "age").send_keys("22")
    add_btn.click()
    user_info = wait_all_5(browser,(By.CSS_SELECTOR, "tbody>tr>td"))

    assert user_info[0].text == "Lena"
    assert user_info[1].text == "Petrova"
    assert user_info[2].text == "22"
    assert len(user_info[3].text) == 36

