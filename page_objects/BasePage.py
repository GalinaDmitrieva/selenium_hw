import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Clicking element: {element}")
    def click(self, element):
        self.logger.info(f" - Clicking element: {element}")
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step("Clicking element: {element}")
    def _input(self, element, value):
        self.logger.info(f" - Input {value} in element {element}")
        self.click(element)
        element.clear()
        element.send_keys(value)

    @allure.step("Check if element {locator} is present")
    def element(self, locator: tuple):
        self.logger.info(f" - Check if element {locator} is present")
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Не дождался видимости элемента {locator}")
