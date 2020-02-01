from selenium import webdriver
import pytest
import time

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from uitlities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems()
        log.info("E2E - Shop menu Page is correctly opened")

        checkoutPage = CheckOutPage(self.driver)
        checkoutPage.clickAddCart() #Add Cart button is clicked
        checkoutPage.openCheckoutPage() #Open Checkout Page Opened
        checkoutPage.clickCheckOutbutton() #CheckOut button is clicked
        log.info("E2E - Product is add to cart")

        confirmationPage = ConfirmationPage(self.driver)
        confirmationPage.inputLocation().send_keys("IND")
        #time.sleep(3)
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        log.info("E2E - INDIA is selected for the delivery")

        confirmationPage.clickPurchaseButton() #Purchase button is clicked
        log.info("testE2E - Order Placed")
        log.info("E2E - Order is placed successfully")

        self.driver.quit()

        #self.driver.find_element_by_xpath("//*[@class='btn btn-success btn-lg']").click()

        #self.driver.find_element_by_xpath("//*[@href= '/angularpractice/shop']").click()
'''     #self.driver.find_element_by_xpath("//*[@class= 'col-lg-9']//*[@class='col-lg-3 col-md-6 mb-3'][1]//*[@class='btn btn-info']").click()
        self.driver.find_element_by_xpath("//*[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//*[@class='btn btn-success']").click()
        self.driver.find_element_by_xpath("//*[@id='country']").send_keys('INDIA')
        self.driver.find_element_by_xpath("//*[@class='btn btn-success btn-lg']").click()
        self.driver.quit()
'''