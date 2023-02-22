
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='button'].btn.btn-default.btn-lg")))
    wait.until(EC.visibility_of_element_located((By.ID, "form-currency")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))


def test_catalog(browser, url):
    browser.get(f'{url}/desktops')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='button'].btn.btn-default")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))
    wait.until(EC.visibility_of_element_located((By.ID, "list-view")))
    wait.until(EC.visibility_of_element_located((By.ID, "grid-view")))


def test_card(browser, url):
    browser.get(f'{url}/desktops/htc-touch-hd?sort=p.sort_order&order=ASC')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "atc_s.addthis_button_compact")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-quantity")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rating")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nav.nav-tabs")))


def test_admin_page(browser, url):
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))


def test_create_user_page(browser, url):
    browser.get(f'{url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn.btn-primary")))
