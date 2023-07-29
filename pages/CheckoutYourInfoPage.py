from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutYourInfoPage(PageObject):
    url = 'https://www.saucedemo.com/checkout-step-one.html'
    text_cart_title = 'Checkout: Your Information'
    css_checkout_btn = '[name="continue"]'
    text_first_name_required = 'Error: First Name is required'
    css_error_menssage = '[data-test="error"]'

    def __init__(self, driver):
        super(CheckoutYourInfoPage, self).__init__(driver=driver)

    def check_your_info_page(self):
        return self.check_pagge(self.url, self.text_cart_title)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_checkout_btn).click()

    def has_first_name_required_error_menssage(self):
        error_text = self.driver.find_element(By.CSS_SELECTOR,self.css_error_menssage).text
        return error_text == self.text_first_name_required



