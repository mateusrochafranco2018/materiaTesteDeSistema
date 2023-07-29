import time

from pages.MenuPage import MenuPage
from pages.ProductsPage import ProductsPage


class Test3:

    def test_logout_app(self, login_saucedemo):
        menu_page = MenuPage(driver=login_saucedemo.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), 'Menu não está aberto!'
        menu_page.click_logout()
        login_page = login_saucedemo
        assert login_page.is_url_login(), 'Pagina de login não encontrada!'
