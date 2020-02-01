from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//*[@href= '/angularpractice/shop']")
    input_Name = (By.XPATH, "//*[@name='name']")
    input_email = (By.XPATH, "//*[@name='email']")
    input_password = (By.XPATH, "//*[@id='exampleInputPassword1']")
    btn_submit = (By.XPATH, "//*[@class='btn btn-success']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop).click()

    def inputName(self):
        return self.driver.find_element(*HomePage.input_Name)

    def inputEmail(self):
        return self.driver.find_element(*HomePage.input_email)

    def inputPassword(self):
        return self.driver.find_element(*HomePage.input_password)

    def inputSubmit(self):
        return self.driver.find_element(*HomePage.btn_submit)

    #def getGender(self, locator, text):
    #    sel = Select(locator)
    #   sel.select_by_visible_text("Male")

