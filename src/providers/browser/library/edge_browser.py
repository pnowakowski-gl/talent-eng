from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.providers.browser.library.base_browser import BaseBrowserClass


class EdgeBrowser(BaseBrowserClass):
    @classmethod
    def get_driver(cls):
        cls.service_obj = Service(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=cls.service_obj)
