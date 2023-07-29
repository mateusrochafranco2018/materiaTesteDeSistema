import time

from pages.MenuPage import MenuPage
from pages.ProductsPage import ProductsPage

class Test3:

    def test_logout_app(self, login_soucedemo):
        menu_page = MenuPage(driver=login_soucedemo.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), 'Menu não está aberto!'
        menu_page.click_logout()
        login_page = login_soucedemo
        assert login_page.is_url_login(), 'Pagina de login não encontrada!'

