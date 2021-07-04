import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser can be: chrome or firefox",
    )

    parser.addoption(
        "--mode",
        action="store",
        default="headless",
        help="browser mode can be: headless or normal",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    mode = request.config.getoption("--mode")

    geckodriver_path = "/home/aleksey/diploma/geckodriver"
    chromedriver_path = "/home/aleksey/diploma/chromedriver"

    if browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--" + mode)
        chrome_options.add_argument("--disable-setuid-sandbox")
        driver = webdriver.Chrome(
            executable_path=chromedriver_path, options=chrome_options
        )
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "selenoid_firefox":
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "88.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        options = FirefoxOptions()
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options)

        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "jenkins_chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=chromedriver_path,
                                  chrome_options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
