from selenium.webdriver.common.by import By

class Locators:

    # Кнопка "Войти в аккаунт" на странице "https://stellarburgers.nomoreparties.site/"
    BTN_ENTER_ACCOUNT = By.XPATH, "//*[text()='Войти в аккаунт']"

    # Кнопка "Войти" на странице "https://stellarburgers.nomoreparties.site/login"
    BTN_ENTER = (By.XPATH, "//button[text()='Войти']")

    # Поле ввода "email" на странице "https://stellarburgers.nomoreparties.site/login"
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # Поле ввода "пароль" на странице "https://stellarburgers.nomoreparties.site/login"
    INPUT_PASSWORD = By.NAME, "Пароль"

    # Кнопка "Личный кабинет"
    BTN_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"

    # ссылка  "Зарегистрироваться" на странице "https://stellarburgers.nomoreparties.site/login"
    REF_REGISTRATION = By.XPATH, "//a[text()='Зарегистрироваться']"

    # ссылка "Войти" в форме регистрация "https://stellarburgers.nomoreparties.site/register"
    REF_ENTER_FROM_SECTION = By.XPATH, "//a[text()='Войти']"

    # ссылка "Восстановить пароль" на странице "https://stellarburgers.nomoreparties.site/login"
    REF_RESTORE_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']"

    # ссылка "Войти" через Восстановить пароль на странице "https://stellarburgers.nomoreparties.site/forgot-password"
    ENTER_FROM_PASSWORD_RESTORE = By.XPATH, "//a[text()='Войти']"







    BTN_ORDER = \
        By.XPATH, "//button[contains(@class, 'button_button_size_large')]"



    REGISTRATION_NAME = By.XPATH, "//*[text(" \
                                  ")='Имя']/following-sibling::input"



    REGISTRATION_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # вход поле Пароль
    INPUT_PASSWORD = By.NAME, "Пароль"



    # ссылка  Зарегистрироваться
    REF_REGISTRATION = By.XPATH, "//a[text()='Зарегистрироваться']"

    # ссылка  Восстановить пароль
    REF_RESTORE_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']"


    BTN_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']"

    TEXT_PROFILE = By.XPATH, "//*[text()='Профиль']"

    TEST_ENTER_MAIN_PAGE = \
        By.XPATH, "//button[contains(@class,'button_button_size_large')]"

    MSG_ERROR_PASSWORD = By.XPATH, "//*[contains(@class, 'input__error ')]"

    BTN_EXIT_PERSONAL_ACCOUNT = By.XPATH, "//button[text()='Выход']"

    BTN_TRANSIT_TO_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"

    TXT_CONSTRUCT_BURGERS = By.XPATH, "//*[text()='Соберите бургер']"

    LOGO = By.XPATH, \
        "//div[contains(@class, 'AppHeader_header__logo')]/child::a "

    BTN_BUL = By.XPATH, "//span[text()='Булки']/parent::div"

    TXT_BUL = By.XPATH, "//h2[text()='Булки']"

    BTN_SOUSES = By.XPATH, "//span[text()='Соусы']/parent::div"

    TXT_SOUSES = By.XPATH, "//h2[text()='Соусы']"

    BTN_STAFFING = By.XPATH, "//span[text()='Начинки']/parent::div"

    TXT_STAFFING = By.XPATH, "//h2[text()='Начинки']"

    VALUE_EMAIL = By.NAME, "name"
