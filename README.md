Клонируйте репозиторий

Установите зависимости

pip install -r requirements.txt

Установите браузеры Playwright

playwright install

Запустите тесты

Все тесты с подробным выводом

pytest tests/ -v

Тесты с HTML отчетом

pytest tests/ -v --html=report.html

Тесты с Allure отчетом

pytest tests/ -v --alluredir=allure-results

Просмотр отчетов

HTML отчет - открой файл report.html в браузере

Allure отчет

allure serve allure-results
