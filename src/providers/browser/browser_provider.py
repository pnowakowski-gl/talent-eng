from selenium import webdriver

from src.providers.browser.library.chrome_browser import ChromeBrowser
from src.providers.browser.library.edge_browser import EdgeBrowser
from src.providers.browser.library.firefox_browser import FirefoxBrowser


class BrowserProvider:
    MAPPER = {"chrome": ChromeBrowser, "ff": FirefoxBrowser, "edge": EdgeBrowser}

    @classmethod
    def get_browser(cls, browser_name: str) -> webdriver:
        browser_class = cls.MAPPER.get(browser_name)
        if browser_class is None:
            raise Exception("Browser not registered in the framework.")
        return browser_class.get_driver()
