import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture
def setup():
    login_page = LoginPage()
    yield login_page
    login_page.close()


@pytest.fixture
def login_soucedemo(setup):
    login_page = setup
    login_page.efetuar_login()
    yield login_page


@pytest.fixture
def has_product_in_cart(login_soucedemo):
    product_page = ProductsPage(driver=login_soucedemo.driver)
    product_page.add_random_product_to_cart()
    assert product_page.get_cart_badge() == '1', 'Quntidade de Produto'
    yield product_page
