import allure
from selenium.webdriver.common.by import By

from selenium_hw.page_objects.BasePage import BasePage


class MainPage(BasePage):
    ACCOUNT_MENU = (By.CSS_SELECTOR, "li.dropdown > a")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    CURRENCY_MENU = (By.ID, "form-currency")
    EUR_OPTION = (By.XPATH, "//button[text()='€ Euro']")
    GBR_OPTION = (By.XPATH, "//button[text()='£ Pound Sterling']")
    USD_OPTION = (By.XPATH, "//button[text()='$ US Dollar']")
    LOGO = (By.ID, "logo")
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default.btn-lg")
    NON_EXISTED_ELEM = (By.ID, "non-existed-elem")

    CART_LIST = (By.ID, "cart")

    @allure.step("I open Account menu")
    def open_account_menu(self):
        self.logger.info("I open Account menu")
        self.click(self.element(self.ACCOUNT_MENU))
        return self

    @allure.step("I open Register form")
    def open_register_form(self):
        self.logger.info("I open Register form")
        self.click(self.element(self.REGISTER_OPTION))
        return self

    @allure.step("I open Currency menu")
    def open_currency_menu(self):
        self.logger.info("I open Currency menu")
        self.click(self.element(self.CURRENCY_MENU))
        return self

    @allure.step("I change currency and check if it is correctly set")
    def change_currency(self, currency):
        self.logger.info(f"I change currency to {currency}")
        if currency == "EUR":
            self.click(self.element(self.EUR_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '€':
                    return self
                else:
                    return AssertionError("Что-то пошло не так")
        elif currency == "GBR":
            self.click(self.element(self.GBR_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '£':
                    return self
                else:
                    return AssertionError("Что-то пошло не так")
        elif currency == "USD":
            self.click(self.element(self.USD_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '$':
                    return self
                else:
                    return AssertionError("Что-то пошло не так")
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Нет такой валюты")
