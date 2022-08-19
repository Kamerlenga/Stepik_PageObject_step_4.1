from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
import time
       
class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage (browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage (browser, browser.current_url)
        login_page.should_be_login_page()
        page.should_be_login_form()
        page.should_be_register_form()
        page.should_be_login_url()
 
