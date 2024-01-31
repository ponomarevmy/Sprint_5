import data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuthorization:
    def test_authorization_from_log_in_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.User.login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.User.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)
        assert btn_is.text == 'Оформить заказ'

    def test_authorization_from_personal_area(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.BTN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.User.login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.User.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)
        assert btn_is.text == 'Оформить заказ'

    def test_authorization_in_registration_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REF_ENTER_FROM_SECTION))
        driver.find_element(*Locators.REF_ENTER_FROM_SECTION).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.User.login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.User.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)
        assert btn_is.text == 'Оформить заказ'

    def test_authorization_password_recovery_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REF_RESTORE_PASSWORD))
        driver.find_element(*Locators.REF_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_FROM_PASSWORD_RESTORE))
        driver.find_element(*Locators.ENTER_FROM_PASSWORD_RESTORE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.User.login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.User.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BTN_ENTER))
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)
        assert btn_is.text == 'Оформить заказ'