# здесь будут храниться фикстуры
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Создание фикстуры, для инициализации драйвера в тестах
@pytest.fixture(scope="function", autouse=True)       # autouse=True - фикстура будет использоваться автоматически для каждого теста; scope="function" - для каждого теста сохдаётся отдельный экземпляр драйвера(открытие браузера)
def driver(request):
    options = Options()         # объект для управления параметрами запуска браузера

    # options.add_argument("--headless")   # Запускает браузер в фоновом режиме без графического интерфейса. Для запуска в CI, Docker

    options.add_argument("--no-sandbox")    # Используется для запуска браузера в контейнере или ограниченной среде. Отключает механизм изоляции браузера в песочнице (sandbox), который является одной из ключевых функций безопасности в браузере Google Chrome.

    options.add_argument("--disable-dev-shm-usage")     # Отключает использование общей памяти /dev/shm. Актуально для ограниченных сред (например, контейнеров).
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)      # инициализируем драйвер
    request.cls.driver = driver     # конструкция создаёт объект драйвера внутри тестов
    yield driver
    driver.quit()

