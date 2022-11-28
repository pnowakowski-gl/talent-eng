from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BaseUIApp:
    """
    Connects abstract methods with selenium tool to automate navigation on the web.
    """

    def __init__(self) -> None:
        self.service_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver.maximize_window()

    def open_page(self, page_name):
        """
        Opens driver page
        """
        self.driver.get(page_name)

    def get_element(self, locator_type: By, locator_name: str):
        """
        Gets element from driver page with locator type and locator name.
        Return webelement.
        """
        return self.driver.find_element(locator_type, locator_name)

    def click(self, locator_type: By, locator_name: str):
        """
        Gets element from driver page with locator type and locator name and click it.
        """
        el = self.driver.find_element(locator_type, locator_name)
        el.click()

    def enter_text(self, locator_type: By, locator_name: str, text: str):
        """
        Gets element from driver page with locator type and locator name and types given text.
        """
        el = self.driver.find_element(locator_type, locator_name)
        el.send_keys(text)
