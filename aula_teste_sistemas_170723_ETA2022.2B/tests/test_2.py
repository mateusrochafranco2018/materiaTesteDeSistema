import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Test2:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield

        self.driver.quit()

    def test_realizar_login(self, setup):
        campo_user_name = self.driver.find_element(By.ID, 'user-name')
        campo_user_name.send_keys("standard_user")

        campo_password = self.driver.find_element(By.ID, 'password')
        campo_password.send_keys("secret_sauce")

        botao = self.driver.find_element(By.ID, 'login-button')

        botao.click()

        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', "Pagina nao mudou !!!"
        title_page = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert title_page == 'Products', 'Titulo da pagina diferente de Products'

        products_list = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(products_list) == 6, 'Lista de produtos incorreto !!!'

        try:
            assert self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), 'Menu nao encontrado !!!'
        except NoSuchElementException:
            pytest.fail('Elemento nao encontrado !!!')
