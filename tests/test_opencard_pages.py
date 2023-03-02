import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from selenium_hw.page_objects.AdminHomePage import AdminHomePage
from selenium_hw.page_objects.AdminPage import AdminPage
from selenium_hw.page_objects.CatalogUserView import CatalogUserView
from selenium_hw.page_objects.MainPage import MainPage
from selenium_hw.page_objects.ProductCardAdminView import ProductCardAdminView
from selenium_hw.page_objects.ProductCardUserView import ProductCardUserView
from selenium_hw.page_objects.RegisterUserPage import RegisterUserPage


@allure.title("Check some existed elements on main page")
def test_existed_elem_main_page(browser, url):
    """Check some elements on main page"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).element(MainPage(browser).LOGO)
    MainPage(browser).element(MainPage(browser).SEARCH_FIELD)
    MainPage(browser).element(MainPage(browser).SEARCH_BUTTON)
    MainPage(browser).element(MainPage(browser).CURRENCY_MENU)
    MainPage(browser).element(MainPage(browser).CART_LIST)
    time.sleep(10)


@allure.title("Check some existed elements on Catalog page for user")
def test_existed_elem_catalog(browser, url):
    """Check some elements on Catalog page for user"""
    browser.get(f'{url}/desktops')
    wait = WebDriverWait(browser, 5)
    CatalogUserView(browser).element(CatalogUserView(browser).NAVIGATION_PANE)
    CatalogUserView(browser).element(CatalogUserView(browser).DEFAULT_VIEW_OPTION)
    CatalogUserView(browser).element(CatalogUserView(browser).SORT_LIST)
    CatalogUserView(browser).element(CatalogUserView(browser).LIST_VIEW_OPTION)
    CatalogUserView(browser).element(CatalogUserView(browser).GRID_VIEW_OPTION)


@allure.title("Check some existed elements on Product card page for user")
def test_existed_elem_card(browser, url):
    """Check some elements on Product card page for user"""
    browser.get(f'{url}/desktops/htc-touch-hd?sort=p.sort_order&order=ASC')
    wait = WebDriverWait(browser, 5)
    ProductCardUserView(browser).element(ProductCardUserView(browser).ADD_TO_CART_BUTTON)
    ProductCardUserView(browser).element(ProductCardUserView(browser).SHARE_BUTTON)
    ProductCardUserView(browser).element(ProductCardUserView(browser).QUANTITY_FIELD)
    ProductCardUserView(browser).element(ProductCardUserView(browser).COMMON_FIELD_RATING)
    ProductCardUserView(browser).element(ProductCardUserView(browser).TABS_PANE)


@allure.title("Check some existed elements on admin authorization page ")
def test_existed_elem_admin_page(browser, url):
    """ Check some elements on admin authorization page """
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser).element(AdminPage(browser).ADMIN_USERNAME)
    AdminPage(browser).element(AdminPage(browser).ADMIN_PASSWORD)
    AdminPage(browser).element(AdminPage(browser).FORGOTTEN_PSWD_LINK)
    AdminPage(browser).element(AdminPage(browser).LOGIN_BTN)
    AdminPage(browser).element(AdminPage(browser).OPENCART_LINK)


@allure.title("Check some existed elements on user creation page")
def test_existed_elem_create_user_page(browser, url):
    """Check some elements on user creation page"""
    browser.get(f'{url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    RegisterUserPage(browser).element(RegisterUserPage(browser).FIRST_NAME)
    RegisterUserPage(browser).element(RegisterUserPage(browser).LAST_NAME)
    RegisterUserPage(browser).element(RegisterUserPage(browser).EMAIL)
    RegisterUserPage(browser).element(RegisterUserPage(browser).PASSWORD)
    RegisterUserPage(browser).element(RegisterUserPage(browser).CONTINUE_BUTTON)


@allure.title("Check successful addition a product in product list")
def test_add_product_to_list(browser, url):
    """Check successful addition a product in product list"""
    prod_name = 'test_product_123'
    meta_tags = 'meta_tags_123'
    model = 'model123'

    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami')

    AdminHomePage(browser). \
        open_catalog_menu(). \
        open_product_list(). \
        open_product_form()

    ProductCardAdminView(browser). \
        fill_mandatory_fields(product_name=prod_name, meta_tag_title=meta_tags, model=model). \
        save_product()

    AdminHomePage(browser). \
        open_product_list()

    ProductCardAdminView(browser). \
        find_product_in_list_by_name(product_name=prod_name)


@allure.title("Check the product deletion (by product name)")
def test_delete_product_by_name(browser, url):
    """Check the product deletion (by product name)"""
    prod_name = 'test_product_123'

    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami')

    AdminHomePage(browser). \
        open_catalog_menu(). \
        open_product_list()

    ProductCardAdminView(browser). \
        remove_product_from_list_by_name(product_name=prod_name)


@allure.title("Creation of new user with valid credentials")
def test_create_new_valid_user(browser, url):
    """Check creation a valid user"""
    f_name = "test"
    l_name = "test"
    email = "test4@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"

    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser).fill_mandatory_fields_for_user(f_name=f_name,
                                                             l_name=l_name,
                                                             email=email,
                                                             phone=phone,
                                                             pswd=pswd,
                                                             pswd_conf=pswd_conf).success_created_user()


@allure.title("Check currency changing on main page to valid one")
@pytest.mark.parametrize('currency', ['EUR', 'USD', 'GBR', 'invalid'])
def test_valid_change_currency(browser, url, currency):
    """Check currency changing on main page to valid one"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_currency_menu().change_currency(currency=currency)
