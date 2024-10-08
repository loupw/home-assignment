import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.step("Find element {locator}")
def find_el(driver, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    return driver.find_element(*locator)

@allure.step("Find elements {locator}")
def find_els(driver, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))
    return driver.find_elements(*locator)

@allure.step("Click element")
def click_el(driver, el, new_window=False):
    open_windows = driver.window_handles
    if type(el) is tuple:
        el = find_el(driver, el)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(el))
    ActionChains(driver).move_to_element(el).click(el).perform()
    if new_window:
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(open_windows))
    return el

if __name__ == "__main__":
    print("For import only!")
