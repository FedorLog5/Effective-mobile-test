from playwright.sync_api import Page, expect
import time
import re

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.effective-mobile.ru"
        
        # Основные элементы
        self.hero_section = page.locator("section.relative.min-h-screen")  # Первая секция с градиентом
        self.header = page.locator("header")
        self.footer = page.locator("footer.bg-bg-primary")
        
        # Кнопки навигации - ищем по тексту
        self.apply_button_header = page.get_by_role("button", name="Оставить заявку")
        
        # Форма обратной связи - ТОЧНЫЙ локатор из HTML
        self.contact_form = page.locator("form.space-y-6")
        self.name_field = page.locator("input[name='name']")
        self.email_field = page.locator("input[name='email'], input[type='email']")
        self.phone_field = page.locator("input[name='phone'], input[type='tel']")
        self.message_field = page.locator("textarea[name='message']")
        self.submit_button = page.get_by_role("button", name="Отправить заявку")
        
        # Разделы страницы - по ID и классам
        self.about_section = page.locator("section.py-24.bg-bg-primary")  # Секция "О компании"
        self.services_section = page.locator("section#services")  # Секция услуг
        self.specialists_section = page.locator("section.py-24.bg-bg-secondary")  # Секция "Кого мы ищем"
        self.contact_section = page.locator("section#contact")  # Контактная секция
        
        # Якорные ссылки
        self.services_link = page.locator("a[href='#services']")
        self.contact_link = page.locator("a[href='#contact']")

    def navigate(self):
        """Переход на главную страницу"""
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")
        time.sleep(2)

    def click_services_link(self):
        """Клик по ссылке на услуги"""
        self.services_link.first.click()
        time.sleep(1)

    def click_contact_link(self):
        """Клик по ссылке на контакты"""
        self.contact_link.first.click()
        time.sleep(1)

    def click_apply_button_header(self):
        """Клик по кнопке 'Оставить заявку' в хедере"""
        self.apply_button_header.first.click()
        time.sleep(1)

    def navigate_to_contact_form(self):
        """Перейти к форме обратной связи"""
        self.click_contact_link()

    def is_section_visible(self, section_name):
        """Проверить видимость секции"""
        section_map = {
            "about": self.about_section,
            "services": self.services_section,
            "specialists": self.specialists_section,
            "contact": self.contact_section
        }
        
        if section_name in section_map:
            return section_map[section_name].is_visible()
        return False

    def is_form_visible(self):
        """Проверить видимость формы"""
        return self.contact_form.is_visible()

    def is_form_field_visible(self, field_type):
        """Проверить видимость поля формы"""
        field_map = {
            "name": self.name_field,
            "email": self.email_field,
            "phone": self.phone_field,
            "message": self.message_field
        }
        
        if field_type in field_map:
            return field_map[field_type].is_visible()
        return False

    def fill_contact_form(self, name="Тест", email="test@test.com", phone="+79999999999", message="Тестовое сообщение"):
        """Заполнить форму обратной связи"""
        if self.name_field.is_visible():
            self.name_field.fill(name)
        if self.email_field.is_visible():
            self.email_field.fill(email)
        if self.phone_field.is_visible():
            self.phone_field.fill(phone)
        if self.message_field.is_visible():
            self.message_field.fill(message)

    def get_current_url(self):
        """Получить текущий URL"""
        return self.page.url

    def take_screenshot(self, name):
        """Создать скриншот"""
        self.page.screenshot(path=f"screenshots/{name}.png")