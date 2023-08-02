import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    """DOC!!!"""
    #version = "114.0.5735.90"
    driver_service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
