import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_hw.page_objects.BasePage import BasePage
from selenium_hw.page_objects.AdminPage import AdminPage
from selenium_hw.page_objects.ProductCard import ProductCard
from selenium_hw.page_objects.MainPage import MainPage
from selenium_hw.page_objects.RegisterPage import RegisterPage
from selenium_hw.page_objects.ProductCardUserView import ProductCardUserView
from selenium_hw.page_objects.CatalogUserView import CatalogUserView


def test_main_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(MainPage(browser).LOGO))
    wait.until(EC.visibility_of_element_located(MainPage(browser).SEARCH_FIELD))
    wait.until(EC.visibility_of_element_located(MainPage(browser).SEARCH_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage(browser).CURRENCY_MENU))
    wait.until(EC.visibility_of_element_located(MainPage(browser).CART_LIST))


def test_catalog(browser, url):
    browser.get(f'{url}/desktops')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(CatalogUserView(browser).NAVIGATION_PANE))
    wait.until(EC.visibility_of_element_located(CatalogUserView(browser).DEFAULT_VIEW_OPTION))
    wait.until(EC.visibility_of_element_located(CatalogUserView(browser).SORT_LIST))
    wait.until(EC.visibility_of_element_located(CatalogUserView(browser).LIST_VIEW_OPTION))
    wait.until(EC.visibility_of_element_located(CatalogUserView(browser).GRID_VIEW_OPTION))


def test_card(browser, url):
    browser.get(f'{url}/desktops/htc-touch-hd?sort=p.sort_order&order=ASC')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(ProductCardUserView(browser).ADD_TO_CART_BUTTON))
    wait.until(EC.visibility_of_element_located(ProductCardUserView(browser).SHARE_BUTTON))
    wait.until(EC.visibility_of_element_located(ProductCardUserView(browser).QUANTITY_FIELD))
    wait.until(EC.visibility_of_element_located(ProductCardUserView(browser).COMMON_FIELD_RATING))
    wait.until(EC.visibility_of_element_located(ProductCardUserView(browser).TABS_PANE))


def test_add_product_to_list(browser, url):
    prod_name = 'test_product_123'
    meta_tags = 'meta_tags_123'
    model = 'model123'

    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami'). \
        open_catalog_menu(). \
        open_product_list(). \
        open_product_form()

    ProductCard(browser). \
        fill_mandatory_fields(product_name=prod_name, meta_tag_title=meta_tags, model=model). \
        save_product()

    AdminPage(browser). \
        open_product_list()

    ProductCard(browser).find_product_in_list_by_name(product_name=prod_name)


def test_delete_product_by_name(browser, url):
    prod_name = 'test_product_123'

    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami'). \
        open_catalog_menu(). \
        open_product_list()

    ProductCard(browser). \
        remove_product_from_list_by_name(product_name=prod_name)


def test_create_new_user(browser, url):
    f_name = "test"
    l_name = "test"
    email = "test3@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"

    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterPage(browser).fill_mandatory_fields_for_user(f_name=f_name,
                                                         l_name=l_name,
                                                         email=email,
                                                         phone=phone,
                                                         pswd=pswd,
                                                         pswd_conf=pswd_conf).success_created_user()


def test_change_currency(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_currency_menu().change_currency(currency="EUR")


def test_admin_page(browser, url):
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(AdminPage(browser).ADMIN_USERNAME))
    wait.until(EC.visibility_of_element_located(AdminPage(browser).ADMIN_PASSWORD))
    wait.until(EC.visibility_of_element_located(AdminPage(browser).FORGOTTEN_PSWD_LINK))
    wait.until(EC.visibility_of_element_located(AdminPage(browser).LOGIN_BTN))
    wait.until(EC.visibility_of_element_located(AdminPage(browser).OPENCART_LINK))


def test_create_user_page(browser, url):
    browser.get(f'{url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(RegisterPage(browser).FIRST_NAME))
    wait.until(EC.visibility_of_element_located(RegisterPage(browser).LAST_NAME))
    wait.until(EC.visibility_of_element_located(RegisterPage(browser).EMAIL))
    wait.until(EC.visibility_of_element_located(RegisterPage(browser).PASSWORD))
    wait.until(EC.visibility_of_element_located(RegisterPage(browser).CONTINUE_BUTTON))
