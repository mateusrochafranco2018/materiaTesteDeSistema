
from pages.YourCartPage import YourCartPage


class Test6:

    def test_add_product_to_cart(self, has_product_in_cart):
        product_page, product_name = has_product_in_cart
        product_page.open_cart()
        your_cart_page = YourCartPage(driver=product_page.driver)
        assert your_cart_page.check_your_cart_page(), 'Your Cart page not found!'
        assert your_cart_page.check_product_name_in_cart(product_name), 'Product name not found!'




