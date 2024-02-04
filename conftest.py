import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get(Urls.url_main)
    yield driver
    driver.quit()
