import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавляем опцию --language для командной строки"""
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, es, fr etc.')


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для создания и закрытия браузера"""
    # Получаем параметр language из командной строки
    user_language = request.config.getoption('--language')

    # Настраиваем опции браузера с выбранным языком
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print(f"\nЗапуск браузера с параметром языка: {user_language}")
    browser = webdriver.Chrome(options=options)

    # Передаём браузер в тест
    yield browser

    # Закрываем браузер после завершения теста
    print("\nЗакрытие браузера...")
    browser.quit()