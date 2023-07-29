import time

import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture
def setup():
    login_page = LoginPage()
    yield login_page
    login_page.close()


@pytest.fixture
def login_saucedemo(setup):
    login_page = setup
    login_page.efetuar_login()
    yield login_page


@pytest.fixture
def has_product_in_cart(login_saucedemo):
    product_page = ProductsPage(driver=login_saucedemo.driver)
    product_page.add_random_product_to_cart()
    assert product_page.get_cart_badge_number() == 1, 'Quantidade de produtos no carrinho está incorreta!'
    yield product_page

