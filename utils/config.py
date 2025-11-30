import os
from typing import Dict, Any

class Config:
    """Конфигурация для тестов"""
    
    BASE_URL = "https://effective-mobile.ru"
    TIMEOUT = 30000  # 30 секунд
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    
    # Настройки Allure
    ALLURE_RESULTS_DIR = "allure-results"
    
    @classmethod
    def get_playwright_config(cls) -> Dict[str, Any]:
        """Получить конфигурацию для Playwright"""
        return {
            "headless": cls.HEADLESS,
            "slow_mo": cls.SLOW_MO,
            "timeout": cls.TIMEOUT
        }