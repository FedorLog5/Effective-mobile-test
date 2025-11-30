Клонируй репозиторий
git clone https://github.com/yourusername/effective-mobile-test.git
cd effective-mobile-test

Установи зависимости
pip install -r requirements.txt

Установи браузеры Playwright
playwright install

Запусти тесты
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
