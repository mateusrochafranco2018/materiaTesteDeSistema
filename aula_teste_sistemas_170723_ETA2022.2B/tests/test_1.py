import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test1:
    @pytest.fixture
    def setup(self):
        # 1 - abrir o browser
        self.driver = webdriver.Chrome()

        # 2 - navegar ate o site desejado
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield

        self.driver.quit()

    def test_click_login_btn(self, setup):
        # 3 - Encontrar o elemento que estou querendo pesquisar
        botao = self.driver.find_element(By.ID, 'login-button')

        # 4 - Clicar elemento que pesquisei no passo 3
        botao.click()

        # 5 - Verificar se continua na mesma pagina
        assert self.driver.current_url == 'https://www.saucedemo.com/', "Pagina mudou !!!"

        # 6 - Procurar o elemento no caso mensagem de erro
        error_mensage = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text

        # 7 Validar o elemento que foi procurado no passo 6
        assert error_mensage == 'Epic sadface: Username is required', 'Mensagem não encontrtrada !!!'
