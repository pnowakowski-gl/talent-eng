from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseUIApp:
    """
    Connects abstract methods with selenium tool to automate navigation on the web.
    """

    def __init__(self, driver) -> None:
        self.driver = driver
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

    def wait_for_element_to_be_present(self, locator_type, locator_name, timer=10):
        WebDriverWait(self.driver, timer).until(
            EC.presence_of_element_located(
                (
                    locator_type,
                    locator_name,
                )
            )
        )

    def close_browser(self):
        self.driver.close()
