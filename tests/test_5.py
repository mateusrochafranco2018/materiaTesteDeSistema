from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from pages.YourCartPage import YourCartPage


class Test5:

    def test_buy_product(self, has_product_in_cart):
        product_page, product_name = has_product_in_cart
        product_page.open_cart()
        your_cart_page = YourCartPage(driver=product_page.driver)
        assert your_cart_page.check_your_cart_page(), 'Your Cart page not found!'
        your_cart_page.click_checkout()
        checkout_your_info_page = CheckoutYourInfoPage(driver=your_cart_page.driver)
        assert checkout_your_info_page.check_checkout_your_info_page(), 'Checkout Your Info page not found!'
        checkout_your_info_page.fill_your_information()
        checkout_your_info_page.click_continue()
        checkout_page = CheckoutOverviewPage(driver=checkout_your_info_page.driver)
        assert checkout_page.check_checkout_page(), 'Checkout Overview page not found!'
        assert checkout_page.check_product_information(product_name), 'Checkout Overview information is not correct!'
        checkout_page.click_finish_btn()
        checkout_complete_page = CheckoutCompletePage(driver=checkout_page.driver)
        assert checkout_complete_page.check_checkout_complete_page(), 'Checkout Complete page not found!'
        assert checkout_complete_page.check_thank_order(), 'Thank you order message not found!'
