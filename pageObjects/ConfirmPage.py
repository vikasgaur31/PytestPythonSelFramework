from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self,driver):
        self.driver = driver

    sendLocation = (By.XPATH, "//*[@id='country']")
    clickPurchaseBtn = (By.XPATH, "//*[@class='btn btn-success btn-lg']")

    def inputLocation(self):
        return self.driver.find_element(*ConfirmationPage.sendLocation)

    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmationPage.clickPurchaseBtn).click()
