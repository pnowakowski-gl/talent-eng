from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from src.providers.browser.library.base_browser import BaseBrowserClass


class FirefoxBrowser(BaseBrowserClass):
    @classmethod
    def get_driver(cls):
        cls.service_obj = Service(GeckoDriverManager().install())
        return webdriver.Firefox(service=cls.service_obj)
