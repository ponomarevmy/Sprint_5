# Яндекс практикум Sprint_5

<h2>Привет! Это авто-тесты для сайта stellarburgers, ниже описаны реализованные методы</h2>

Регистрация - `test_registration.py`
<table>
	<tbody>
		<tr>
			<td>test_reg_success</td>
			<td>Проверка успешной регистрации.</td>
		</tr>
		<tr>
			<td>test_reg_password_not_correct</td>
			<td>Регистрация не возможна если пароль меньше 6 символов.</td>
		</tr>
	</tbody>
</table>

Вход -  `test_authorization.py`
<table>
	<tbody>
		<tr>
			<td>test_authorization_from_log_in_account</td>
			<td>Вход по кнопке «Войти в аккаунт» на главной.</td>
		</tr>
		<tr>
			<td>test_authorization_from_personal_area</td>
			<td>Вход через кнопку «Личный кабинет.</td>
		</tr>
		<tr>
			<td>test_authorization_in_registration_form</td>
			<td>Вход через кнопку в форме регистрации.</td>
		</tr>
		<tr>
			<td>test_authorization_password_recovery_form</td>
			<td>Вход через кнопку в форме восстановления пароля.</td>
		</tr>
	</tbody>
</table>

Переход в личный кабинет - `test_go_to_personal_account.py`
<table>
	<tbody>
		<tr>
			<td>test_personal_account</td>
			<td>Переход по клику на «Личный кабинет».</td>
		</tr>
	</tbody>
</table>

Переход из личного кабинета в конструктор - `test_go_to_constructor_from_personal_account.py`
<table>
	<tbody>
		<tr>
			<td>test_go_to_constructor</td>
			<td>Переход по клику на «Конструктор» и на логотип Stellar Burgers из личного кабинета</td>
		</tr>
	</tbody>
</table>

Выход из аккаунта - `test_logout.py`
<table>
	<tbody>
		<tr>
			<td>test_logout</td>
			<td>Выход по кнопке «Выйти» в личном кабинете.</td>
		</tr>
	</tbody>
</table>

Раздел «Конструктор» - `test_section_constructor.py`
<table>
	<tbody>
		<tr>
			<td>test_constructor_section_burgers</td>
			<td>Переходы к разделу "Булки":</td>
		</tr>
		<tr>
			<td>test_constructor_section_souses</td>
			<td>Переходы к разделу "Соусы"</td>
		</tr>
		<tr>
			<td>test_constructor_section_staffing</td>
			<td>Переходы к разделу "Начинки"</td>
		</tr>
	</tbody>
</table>
<br>
<h3>Для работы нужны библиотеки:</h3>
<h4>1 - Selenium</h4>
<h4>2 - Pytest</h4>
Запуск тестов `pytest -v`