

from pages.ProductsPage import ProductsPage


class Test7:

    def test_filtrar_produtos_low_to_high(self, login_saucedemo):
        products_page = ProductsPage(driver=login_saucedemo.driver)
        assert products_page.check_product_pages(), 'Product page not found'
        products_page.filtrar_opcao_lohi()
        assert products_page.check_order_by_price_low_to_high(), 'Incorrect price order'

