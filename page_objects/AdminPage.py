import time

from selenium.webdriver.common.by import By
from selenium_hw.page_objects.BasePage import BasePage


class AdminPage(BasePage):

    ADMIN_USERNAME = (By.ID, "input-username")
    ADMIN_PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    CATALOG_MENU = (By.LINK_TEXT, "Catalog")
    PRODUCTS_OPTION = (By.LINK_TEXT, "Products")
    ADD_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    FORGOTTEN_PSWD_LINK = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, "OpenCart")

    def login(self, username, password):
        self._input(self.element(self.ADMIN_USERNAME), username)
        self._input(self.element(self.ADMIN_PASSWORD), password)
        self.click(self.element(self.LOGIN_BTN))
        return self

    def open_catalog_menu(self):
        self.click(self.element(self.CATALOG_MENU))
        return self

    def open_product_list(self):
        self.click(self.element(self.PRODUCTS_OPTION))
        return self

    def open_product_form(self):
        self.click(self.element(self.ADD_BUTTON))
        return self








