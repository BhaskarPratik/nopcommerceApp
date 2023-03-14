import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        print("Launching firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Lunching edge browser")
    else:
        driver = webdriver.Ie()
        print("Lunching Internet Explorer")
    return driver


# ====================browser code==============================
def pytest_addoption(parser):  # This will get the value from CLI hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption("--browser")


# ======================Pytest Html report ==========================
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Pratik'


@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
