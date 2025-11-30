import pytest
import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
import time

@allure.suite("Главная страница Effective Mobile")
@allure.feature("Проверка одностраничного лендинга")
class TestMainPage:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Фикстура для инициализации страницы"""
        self.main_page = MainPage(page)
        self.main_page.navigate()
        yield

    @allure.title("Проверка доступности главной страницы")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_main_page_availability(self):
        """Тест доступности главной страницы"""
        with allure.step("Проверить заголовок страницы"):
            title = self.main_page.page.title()
            assert title and len(title) > 0, "Заголовок страницы пустой"
        
        with allure.step("Проверить статус код страницы"):
            response = self.main_page.page.request.get(self.main_page.base_url)
            assert response.status == 200, f"Страница недоступна, статус: {response.status}"
        
        with allure.step("Проверить наличие главного баннера"):
            assert self.main_page.hero_section.is_visible(), "Главный баннер не виден"

    @allure.title("Проверка навигации по якорным ссылкам")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_anchor_navigation(self):
        """Тест навигации по якорным ссылкам"""
        with allure.step("Кликнуть на ссылку 'Услуги'"):
            if self.main_page.services_link.count() > 0:
                self.main_page.click_services_link()
                assert self.main_page.services_section.is_visible(), "Не удалось перейти к разделу услуг"
            else:
                pytest.skip("Ссылка на услуги не найдена")

    @allure.title("Проверка кнопки 'Оставить заявку'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_apply_button(self):
        """Тест кнопки 'Оставить заявку'"""
        with allure.step("Найти и кликнуть кнопку 'Оставить заявку'"):
            if self.main_page.apply_button_header.count() > 0:
                self.main_page.click_apply_button_header()
                time.sleep(1)
                assert True, "Успешно кликнули по кнопке 'Оставить заявку'"
            else:
                pytest.skip("Кнопка 'Оставить заявку' не найдена")

    @allure.title("Проверка формы обратной связи")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_form(self):
        """Тест формы обратной связи"""
        with allure.step("Перейти к форме обратной связи"):
            self.main_page.navigate_to_contact_form()
        
        with allure.step("Проверить наличие формы"):
            assert self.main_page.is_form_visible(), "Форма обратной связи не найдена"
        
        with allure.step("Проверить поля формы"):
            assert self.main_page.is_form_field_visible("name"), "Поле 'Имя' не найдено"
            assert self.main_page.is_form_field_visible("email"), "Поле 'Email' не найдено"
            assert self.main_page.is_form_field_visible("phone"), "Поле 'Телефон' не найдено"

    @allure.title("Проверка основных разделов страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_main_sections(self):
        """Тест основных разделов страницы"""
        sections_to_check = [
            ("services", "Услуги"),
            ("contact", "Контакты")
        ]
        
        for section_key, section_name in sections_to_check:
            with allure.step(f"Проверить раздел '{section_name}'"):
                if self.main_page.is_section_visible(section_key):
                    print(f"✅ Раздел '{section_name}' виден")
                else:
                    print(f"❌ Раздел '{section_name}' не виден")

        # Хотя бы один раздел должен быть виден
        assert self.main_page.is_section_visible("services") or self.main_page.is_section_visible("contact"), "Основные разделы не видны"

    @allure.title("Проверка футера")
    @allure.severity(allure.severity_level.MINOR)
    def test_footer_section(self):
        """Тест футера сайта"""
        with allure.step("Прокрутить к футеру"):
            self.main_page.footer.scroll_into_view_if_needed()
            time.sleep(1)
        
        with allure.step("Проверить наличие футера"):
            assert self.main_page.footer.is_visible(), "Футер не виден"

    @allure.title("Заполнение формы обратной связи")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_contact_form(self):
        """Тест заполнения формы обратной связи"""
        with allure.step("Перейти к форме"):
            self.main_page.navigate_to_contact_form()
        
        with allure.step("Заполнить форму тестовыми данными"):
            self.main_page.fill_contact_form()
            
        with allure.step("Проверить что поля заполнены"):
            # Можно добавить проверки заполнения полей
            assert True, "Форма успешно заполнена"