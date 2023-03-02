import allure
from selenium.webdriver.common.by import By

from selenium_hw.page_objects.BasePage import BasePage


class RegisterUserPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, "input-password")
    PASSWORD_CONFIRM = (By.ID, "input-confirm")
    PP_CHECK = (By.CSS_SELECTOR, "input[type='checkbox']")
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn.btn-primary")

    @allure.step("I create new user")
    def fill_mandatory_fields_for_user(self, f_name, l_name, email, phone, pswd, pswd_conf):
        self.logger.info("I fill Register form for user")
        self._input(self.element(self.FIRST_NAME), f_name)
        self._input(self.element(self.LAST_NAME), l_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), phone)
        self._input(self.element(self.PASSWORD), pswd)
        self._input(self.element(self.PASSWORD_CONFIRM), pswd_conf)
        self.logger.info("I agree with PP")
        self.click(self.element(self.PP_CHECK))
        self.logger.info("I click on Continue button")
        self.click(self.element(self.CONTINUE_BUTTON))
        return self

    @allure.step("I check that user is successfully created")
    def success_created_user(self):
        self.logger.info("I check that user is successfully created")
        txt = self.driver.find_element(By.CSS_SELECTOR, "div[id='content'].col-sm-9 > h1")
        if txt.text == "Your Account Has Been Created!":
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Пользователь не создан")
