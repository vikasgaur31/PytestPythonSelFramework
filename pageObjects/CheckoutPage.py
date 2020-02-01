from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    clickAddCartLink = (By.XPATH, "//*[@class= 'col-lg-9']//*[@class='col-lg-3 col-md-6 mb-3'][1]//*[@class='btn btn-info']")
    clickCheckoutLink = (By.XPATH, "//*[@class='nav-link btn btn-primary']")
    clickCheckoutbutton = (By.XPATH, "//*[@class='btn btn-success']")


    #def getCardTitle(self):
        #return self.driver.find_element(*CheckOutPage.cardTitle)

    def clickAddCart(self):
        return self.driver.find_element(*CheckOutPage.clickAddCartLink).click()

    def openCheckoutPage(self):
        return self.driver.find_element(*CheckOutPage.clickCheckoutLink).click()

    def clickCheckOutbutton(self):
        return self.driver.find_element(*CheckOutPage.clickCheckoutbutton).click()
