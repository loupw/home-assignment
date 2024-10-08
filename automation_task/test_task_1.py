import allure
import pytest
import locators
from helpers import find_els


@pytest.mark.parametrize("locator", [locators.dropdown_xpath, locators.dropdown_css])
@allure.title("Find Dpopdown by {locator[0]} locator")
def test_dropdown(driver_setup_shudown, locator):
    driver = driver_setup_shudown
    driver.get("https://staging.tokensfarm.com/create#/staking")

    dropdown = find_els(driver, locator)
    assert dropdown, "Dropdown not found!"
