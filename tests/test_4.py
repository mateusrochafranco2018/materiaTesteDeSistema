
class Test4:

    def test_verify_error_message_in_checkout(self,has_product_in_cart):
        product_page = has_product_in_cart
        product_page.open_cart()
