import pytest
from selenium import webdriver


@pytest.fixture()
def driver_setup_shudown():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
