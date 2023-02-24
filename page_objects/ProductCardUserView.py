import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium_hw.page_objects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class ProductCardUserView(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    SHARE_BUTTON = (By.CLASS_NAME, "atc_s.addthis_button_compact")
    QUANTITY_FIELD = (By.ID, "input-quantity")
    COMMON_FIELD_RATING = (By.CLASS_NAME, "rating")
    TABS_PANE = (By.CLASS_NAME, "nav.nav-tabs")
