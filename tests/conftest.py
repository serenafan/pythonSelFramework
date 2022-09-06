import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # chrome driver to invoke browser
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        service_obj = Service("C:/Users/shuhfan/Documents/python-selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "edge":
        service_obj = Service("C:/Users/shuhfan/Documents/python-selenium/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# setup command line option: pytest -- browser_name edge to invoke edge browser
# https://docs.pytest.org/en/7.1.x/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = 'reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_path = 'screenshots/' + file_name
            _capture_screenshot(file_path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % ("../" + file_path)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    currentDirName = os.path.dirname(__file__)
    filepath = os.path.join(currentDirName, 'screenshots/')
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    driver.get_screenshot_as_file(name)
