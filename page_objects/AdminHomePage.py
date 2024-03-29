from selenium.webdriver.common.by import By

from selenium_hw.page_objects.BasePage import BasePage


class AdminHomePage(BasePage):
    CATALOG_MENU = (By.LINK_TEXT, "Catalog")
    PRODUCTS_OPTION = (By.LINK_TEXT, "Products")
    ADD_BUTTON = (By.CLASS_NAME, "btn.btn-primary")

    def open_catalog_menu(self):
        self.logger.info("I open Catalog menu")
        self.click(self.element(self.CATALOG_MENU))
        return self

    def open_product_list(self):
        self.logger.info("I open Product list page")
        self.click(self.element(self.PRODUCTS_OPTION))
        return self

    def open_product_form(self):
        self.logger.info("I open new product form")
        self.click(self.element(self.ADD_BUTTON))
        return self
