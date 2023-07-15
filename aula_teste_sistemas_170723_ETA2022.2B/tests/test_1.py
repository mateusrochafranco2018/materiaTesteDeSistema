from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.find_element(by='css selector', value='#login-button').click()
driver.quit()
