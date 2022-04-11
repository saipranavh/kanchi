from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        print("Launching chrome browser...")
        driver = webdriver.Chrome(executable_path="C:\\Users\\Arun\\Downloads\\driver\\chromedriver.exe")
    elif browser == "edge":
        print("Launching edge browser...")
        driver = webdriver.Edge(executable_path="C:\\Users\\Arun\\Downloads\\driver\\msedgedriver.exe")
    else:
        print("launching IE browser...")
        driver = webdriver.Ie(executable_path="C:\\Users\\Arun\\Downloads\\driver\\IEDriverServer.exe")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI :command line interpreter/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to the setup method
    return request.config.getoption("--browser")


########pytest html report#############
# It is a hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'sathish'


# It is a hook to delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_home", None)
    metadata.pop("Plugins", None)
