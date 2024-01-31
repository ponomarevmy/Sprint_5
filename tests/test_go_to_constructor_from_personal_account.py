import time
import data
import urls
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoToConstructor:
    def test_go_to_constructor(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.User.login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.User.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_TRANSIT_TO_CONSTRUCTOR))
        driver.find_element(*Locators.BTN_TRANSIT_TO_CONSTRUCTOR).click()
        time.sleep(2)
        current_url = driver.current_url
        assert current_url == urls.Urls.url_main
