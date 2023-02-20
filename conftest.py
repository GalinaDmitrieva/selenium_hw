import os
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver = None
    if _browser == "firefox" or _browser == "ff":
        driver = webdriver.Firefox(executable_path=os.path.expanduser("~/user/drivers/geckodriver"))
    elif _browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("~/user/drivers/chromedriver"))
    elif _browser == "Safari":
        driver = webdriver.Safari()
    yield driver
    driver.close()
