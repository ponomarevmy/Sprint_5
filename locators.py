from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Войти в аккаунт" на странице "https://stellarburgers.nomoreparties.site/"
    BTN_ENTER_ACCOUNT = By.XPATH, "//*[text()='Войти в аккаунт']"

    # Кнопка "Войти" на странице "https://stellarburgers.nomoreparties.site/login"
    BTN_ENTER = (By.XPATH, "//button[text()='Войти']")

    # Поле ввода "email" на странице "https://stellarburgers.nomoreparties.site/login"
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # Поле ввода "пароль" на странице "https://stellarburgers.nomoreparties.site/login" и "register"
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

    # Поле "Имя" на странице "https://stellarburgers.nomoreparties.site/register"
    REGISTRATION_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"

    # Поле "Email" на странице "https://stellarburgers.nomoreparties.site/register"
    REGISTRATION_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"

    # Кнопка "Зарегистрироваться" на странице "https://stellarburgers.nomoreparties.site/register"
    BTN_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']"

    # Сообщение "Некорректный пароль" на странице "https://stellarburgers.nomoreparties.site/register"
    MSG_ERROR_PASSWORD = By.XPATH, "//*[contains(@class, 'input__error ')]"

    # Главный логотип сайта
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/child::a "

    # Раздел "Конструктор"
    BTN_TRANSIT_TO_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"

    # Кнопка "Выход" на странице "https://stellarburgers.nomoreparties.site/account/profile"
    BTN_EXIT_PERSONAL_ACCOUNT = By.XPATH, "//button[text()='Выход']"

    # Кнопка для переключения в раздел "Булки"
    BTN_BUL = By.XPATH, "//span[text()='Булки']/parent::div"

    # Скрол раздела "Булки"
    TXT_BUL = By.XPATH, "//h2[text()='Булки']"

    # Кнопка для переход в раздел "Соусы"
    BTN_SOUSES = By.XPATH, "//span[text()='Соусы']/parent::div"

    # Скрол раздела "Соусы"
    TXT_SOUSES = By.XPATH, "//h2[text()='Соусы']"

    # Кнопка для переход в раздел "Начини"
    BTN_STAFFING = By.XPATH, "//span[text()='Начинки']/parent::div"

    # Скрол раздела "Начинки"
    TXT_STAFFING = By.XPATH, "//h2[text()='Начинки']"

    # Кнопка "Оформить заказ" (После авторизции)
    BTN_ORDER = By.XPATH, "//button[contains(@class, 'button_button_size_large')]"