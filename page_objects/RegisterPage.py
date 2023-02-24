import time

from selenium.webdriver.common.by import By
from selenium_hw.page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, "input-password")
    PASSWORD_CONFIRM = (By.ID, "input-confirm")
    PP_CHECK = (By.CSS_SELECTOR, "input[type='checkbox']")
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn.btn-primary")

    def fill_mandatory_fields_for_user(self, f_name, l_name, email, phone, pswd, pswd_conf):
        self._input(self.element(self.FIRST_NAME), f_name)
        self._input(self.element(self.LAST_NAME), l_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), phone)
        self._input(self.element(self.PASSWORD), pswd)
        self._input(self.element(self.PASSWORD_CONFIRM), pswd_conf)
        self.click(self.element(self.PP_CHECK))
        self.click(self.element(self.CONTINUE_BUTTON))
        return self

    def success_created_user(self):
        txt = self.driver.find_element(By.CSS_SELECTOR, "div[id='content'].col-sm-9 > h1")
        if txt.text == "Your Account Has Been Created!":
            return self
        else:
            raise AssertionError("Пользователь не создан")
