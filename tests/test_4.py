
from pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from pages.YourCartPage import YourCartPage


class Test4:

    def test_verify_error_message_in_checkout(self, has_product_in_cart):
        product_page, product_name = has_product_in_cart
        product_page.open_cart()
        your_cart_page = YourCartPage(driver=product_page.driver)
        assert your_cart_page.check_your_cart_page(), 'Your Cart page not found!'
        your_cart_page.click_checkout()
        checkout_your_info_page = CheckoutYourInfoPage(driver=your_cart_page.driver)
        assert checkout_your_info_page.check_checkout_your_info_page(), 'Checkout Your Info page not found!'
        checkout_your_info_page.click_continue()
        assert checkout_your_info_page.has_first_name_required_error_message(), 'Error message not found!'




