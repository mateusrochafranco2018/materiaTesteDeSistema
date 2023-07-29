from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    txt_products_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu_btn = "react-burger-menu-btn"
    class_prooduct_card = 'inventory_item'
    class_add_to_card_btn = 'btn_primary'
    class_cart_badge = 'shopping_cart_badge'
    class_cart_btn = 'shopping_cart_link'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.driver.current_url == self.url

    def has_products_title(self):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_page == self.txt_products_title

    def validate_products_in_page(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        return len(products_list) == 6

    def has_menu_button(self):
        try:
            return self.driver.find_element(By.ID, self.id_menu_btn).is_displayed()
        except NoSuchElementException:
            return False

    def add_random_product_to_cart(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_prooduct_card)
        random_product = randint(0, len(product_list) - 1)
        product_element = product_list[random_product]
        product_element.find_element(By.CLASS_NAME, self.class_add_to_card_btn).click()

    def get_cart_badge(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_cart_badge).text

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_cart_btn).click()
