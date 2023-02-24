import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium_hw.page_objects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class CatalogUserView(BasePage):

    NAVIGATION_PANE = (By.ID, "column-left")
    DEFAULT_VIEW_OPTION = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default")
    SORT_LIST = (By.ID, "input-sort")
    LIST_VIEW_OPTION = (By.ID, "list-view")
    GRID_VIEW_OPTION = (By.ID, "grid-view")