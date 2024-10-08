from selenium.webdriver.common.by import By


dropdown_xpath = (By.XPATH, '//input[@id="react-select-2-input"]')
dropdown_css = (By.CSS_SELECTOR, "#react-select-2-input")

sidebar = (By.XPATH, '//aside[contains(@class, "duf-aside")]')
sidebar_toggle = (By.XPATH, '//div[@class="passed-content-wrapper"]/div[contains(@class, "sidebar-toggle-wrapper")]')

question = (By.XPATH, '//div[contains(@class, "faq-item-wrapper")]')
question_content = (By.XPATH, '//div[@class="parent-content"]')
question_toggle = (By.XPATH, '//div[@class="pointer"]')

support_btn = (By.XPATH, '//span[text()="Contact Support"]')

if __name__ == "__main__":
    print("For import only!")
