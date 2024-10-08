import allure
import pytest
import locators
from helpers import find_el, find_els, click_el
from questions import questions


@allure.title("Verify Sidebar is expanded")
def test_sidebar_expanded(driver_setup_shudown):
    driver = driver_setup_shudown
    driver.get("https://staging-app.hord.fi/")

    sidebar = find_el(driver, locators.sidebar)
    assert "sidebar-expanded" in str(sidebar.get_attribute("class")), "Sidebar not expanded!"
    assert sidebar.text == 'ETH Staking\nStats\nRevenue Share\nMy Portfolio\nEnglish', "Sidebar not expanded!" 

@allure.title("Verify collapsing of Sidebar")
def test_collapse_sidebar(driver_setup_shudown):
    driver = driver_setup_shudown
    driver.get("https://staging-app.hord.fi/")
    
    click_el(driver, locators.sidebar_toggle)
    sidebar = find_el(driver, locators.sidebar)
    assert "sidebar-expanded" not in str(sidebar.get_attribute("class")), "Sidebar expanded!"
    assert sidebar.text != 'ETH Staking\nStats\nRevenue Share\nMy Portfolio\nEnglish', "Sidebar expanded!" 

@pytest.mark.parametrize("n,text", questions)
@allure.title("Verify Question #{n} in FAQ section")
def test_faq_section(driver_setup_shudown, n, text):
    driver = driver_setup_shudown
    driver.get("https://staging-app.hord.fi/")

    question = find_els(driver, locators.question)[n]
    question_toggle = find_els(driver, locators.question_toggle)[n]
    click_el(driver, question_toggle)
    driver.implicitly_wait(1) # :(
    content = find_els(driver, locators.question_content)[n]
    assert str(content.get_attribute("style")) != "height: 0px;", "Question toggle doesn't work!"
    question = driver.find_elements(*locators.question)[n]
    assert question.text.replace("\n", "") == text, "Title or/and text is incorrect!"

@allure.title("Verify Support button in FAQ section")
def test_faq_support(driver_setup_shudown):
    driver = driver_setup_shudown
    driver.get("https://staging-app.hord.fi/")

    click_el(driver, locators.support_btn, new_window=True)
    assert len(driver.window_handles) == 2, "Chat window don't open!"
    driver.switch_to.window(driver.window_handles[1])
    assert "go.crisp.chat/chat/embed" in driver.current_url, "Chat link is wrong!"
