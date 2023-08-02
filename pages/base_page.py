from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        try:
            element = Wait(self.driver, timeout).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator[1]}"
            )
            return element
        except TimeoutException as e:
            print(e.msg)
            pass

    def find_elements(self, locator, timeout=10):
        try:
            elements = Wait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator[1]}"
            )
            return elements
        except TimeoutException as e:
            print(e.msg)
            pass

    def click_element(self, locator, timeout=10):
        try:
            elements = Wait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator),
                message=f"Can't click element by locator {locator[1]}"
            )
        except TimeoutException as e:
            print(e.msg)
            pass

    def change_to_second_tab(self):
        new_page = self.driver.window_handles[1]
        return self.driver.swith_to.window(new_page)
