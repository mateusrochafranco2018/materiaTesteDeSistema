from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    class_title_page = 'title'

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def has_title(self, title_text):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_page == title_text

    def check_pagge(self, url, title_text):
        return self.is_url(url) and self.has_title(title_text)
