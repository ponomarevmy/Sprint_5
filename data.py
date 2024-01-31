import random as r


class GenLogin:
    name_reg = "Mark"
    login_reg_success = f'mark_ponomarev{r.randint(100, 900)}@yandex.ru'
    password_reg_success = 123456
    password_not_correct = 12345


class User:
    # Для авторизации
    login = 'test_user_3001123@ya.ru'
    password = 123456
