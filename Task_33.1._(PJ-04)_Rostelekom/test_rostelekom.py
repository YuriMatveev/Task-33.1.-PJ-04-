from settings import *
import pytest


# Р-01 Открывается cтраница c формой "Авторизация", вкладка "Телефон".
def test_phone_auth(browser, auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# Р-02 Открывается cтраница c формой "Авторизация", вкладка "Почта".
def test_mail_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# Р-03 Открывается cтраница c формой "Авторизация", вкладка "Логин".
def test_login_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    assert auth.find_element(auth.LOCATOR_BTN_LOGIN)


# Р-04 Открывается cтраница c формой "Авторизация", вкладка "Лицевой счет".
def test_account_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    assert auth.find_element(auth.LOCATOR_BTN_LS)


# Р-05 Вызов формы "Восстановление пароля".
def test_password_recovery_form(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# Р-06 Вызов формы "Регистрация".
def test_registration_form(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# Р-07 Проверка авторизации по телефону и паролю, вкладка "Телефон".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone], ids=['valid phone'])
def test_valid_phone_auth(browser, auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Р-08 Проверка авторизации по телефону и паролю, вкладка "Почта".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone], ids=['valid phone'])
def test_valid_phone_email_auth(browser, auth, username):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Р-09 Проверка авторизации по телефону и паролю, вкладка "Логин".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone], ids=['valid phone'])
def test_valid_phone_login_auth(browser, auth, username):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Р-10 Проверка авторизации по почте и паролю, вкладка "Почта".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_email], ids=['valid email'])
def test_valid_email_auth(browser, auth, username):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Р-11 Проверка авторизации по почте и паролю, вкладка "Телефон".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_email], ids=['valid email'])
def test_valid_email_phone_auth(browser, auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Р-12 Проверка авторизации по почте и паролю, вкладка "Логин".
@pytest.mark.positive
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_email], ids=['valid email'])
def test_valid_email_login_auth(browser, auth, username):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)

# Р-13 Проверка авторизации по телефону и неверному паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone], ids=['valid phone'])
def test_valid_phone_invalid_pass_auth(browser, auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, '1234567890')
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# Р-14 Проверка авторизации по неверному телефону и паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_invalid_phone_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '1234567890')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# Р-15 Проверка авторизации по пустому полю телефон и паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_no_phone_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# Р-16 Проверка авторизации по почте и неверному паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_email], ids=['valid email'])
def test_valid_email_invalid_pass_auth(browser, auth, username):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, '1234567890')
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# Р-17 Проверка авторизации по неверному полю почта и паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_invalid_emeil_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '1234567890')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_CAPTCHA


# Р-18 Проверка авторизации по пустому полю почта и паролю.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_no_emeil_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# Р-19 Проверка авторизации по пустому полю логин и паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_no_login_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# Р-20 Проверка авторизации по пустому полю лицевой счет и паролю. Негативный тест.
@pytest.mark.negative
@pytest.mark.fail_if_captcha
def test_no_ls_valid_pass_auth(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG

