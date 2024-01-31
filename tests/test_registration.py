import data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_reg_success(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_REGISTRATION))
        driver.find_element(*Locators.REGISTRATION_NAME).send_keys(data.GenLogin.name_reg)
        driver.find_element(*Locators.REGISTRATION_EMAIL).send_keys(data.GenLogin.login_reg_success)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.GenLogin.password_reg_success)
        driver.find_element(*Locators.BTN_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.GenLogin.login_reg_success)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.GenLogin.password_reg_success)
        driver.find_element(*Locators.BTN_ENTER).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ORDER))
        btn_is = driver.find_element(*Locators.BTN_ORDER)
        assert btn_is.text == 'Оформить заказ'

    def test_reg_password_not_correct(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_ENTER_ACCOUNT))
        driver.find_element(*Locators.BTN_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REF_REGISTRATION))
        driver.find_element(*Locators.REF_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BTN_REGISTRATION))
        driver.find_element(*Locators.REGISTRATION_NAME).send_keys(data.GenLogin.name_reg)
        driver.find_element(*Locators.REGISTRATION_EMAIL).send_keys(data.GenLogin.login_reg_success)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.GenLogin.password_not_correct)
        driver.find_element(*Locators.BTN_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MSG_ERROR_PASSWORD))
        driver.find_element(*Locators.MSG_ERROR_PASSWORD)
        err_msg = driver.find_element(*Locators.MSG_ERROR_PASSWORD)
        assert err_msg.text == "Некорректный пароль"
