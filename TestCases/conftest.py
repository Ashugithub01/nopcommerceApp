from selenium import webdriver
import pytest

""" @pytest.fixture()
def setup():
    driver = webdriver.Chrome('C://Users//Asheesh//PycharmProjects//driver//chromedriver.exe')
    return driver """



@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome('C://Users//Asheesh//PycharmProjects//driver//chromedriver.exe')
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=r"C:\Users\Asheesh\PycharmProjects\driver\geckodriver.exe")
        driver.maximize_window()
    elif browser == "edge":
       driver = webdriver.Edge('C://Users//Asheesh//PycharmProjects//driver//msedgedriver.exe')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# PyTest HTML Report
# It is hook for Adding Environment info to HTML Report

def pytest_configure (config):
    config. _metadata['Project Name'] = 'DIMS'
    #config. _metadata[ 'Module Name'] = 'Login'
    config. _metadata[ 'Tester'] = 'Asheesh'

# It is hook for delete Modify Environment info to HIML Report

@pytest.mark.optiona_hook
def pytest_metadata (metadata):
    metadata. pop ("JAVA_HOME", None)
    metadata.pop("Plugins", None)

