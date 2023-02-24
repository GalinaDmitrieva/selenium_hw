import time

from selenium.webdriver.common.by import By
from selenium_hw.page_objects.BasePage import BasePage


class MainPage(BasePage):

    ACCOUNT_MENU = (By.CSS_SELECTOR, "li.dropdown > a")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    CURRENCY_MENU = (By.ID, "form-currency")
    EUR_OPTION = (By.XPATH, "//button[text()='€ Euro']")
    GBR_OPTION = (By.XPATH, "//button[text()='£ Pound Sterling']")
    USD_OPTION= (By.XPATH, "//button[text()='$ US Dollar']")
    LOGO = (By.ID, "logo")
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default.btn-lg")

    CART_LIST = (By.ID, "cart")

    def open_account_menu(self):
        self.click(self.element(self.ACCOUNT_MENU))
        return self

    def open_register_form(self):
        self.click(self.element(self.REGISTER_OPTION))
        return self

    def open_currency_menu(self):
        self.click(self.element(self.CURRENCY_MENU))
        return self

    def change_currency(self, currency):
        if currency == "EUR":
            self.click(self.element(self.EUR_OPTION))
            if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '€':
                return self
            else:
                return AssertionError("Что-то пошло не так")
        elif currency == "GBR":
            self.click(self.element(self.GBR_OPTION))
            if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '£':
                return self
            else:
                return AssertionError("Что-то пошло не так")
        elif currency == "USD":
            self.click(self.element(self.USD_OPTION))
            if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '$':
                return self
            else:
                return AssertionError("Что-то пошло не так")
        else:
            raise AssertionError("Нет такой валюты")
        