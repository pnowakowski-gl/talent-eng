from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.providers.browser.library.base_browser import BaseBrowserClass


class ChromeBrowser(BaseBrowserClass):
    @classmethod
    def get_driver(cls):
        cls.service_obj = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=cls.service_obj)
