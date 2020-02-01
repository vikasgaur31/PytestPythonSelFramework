import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from test_data.HomePageData import HomePageData
from uitlities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePagetest = HomePage(self.driver)
        homePagetest.inputName().send_keys(getData["Name"])
        log.info("first name is - "+getData["Name"])
        homePagetest.inputEmail().send_keys(getData["Email"])
        log.info("first name is - "+getData["Email"])
        homePagetest.inputPassword().send_keys(getData["Password"])
        log.info("first name is - "+getData["Password"])

        #self.selectOptionByTest(HomePage.getGender(), "Male")
        homePagetest.inputSubmit().click()
        self.driver.refresh()
        log.info("test_homepage - Order Placed")

    #@pytest.fixture(params=[('Test1', 'test1@xyz.com', '1234'), ('Test2', 'test2@xyz.com', '1234')]) #Data Handling with tuple
    @pytest.fixture(params=HomePageData.test_HomePage_data) #Data Handling with dictonary
    def getData(self, request):
        return request.param


'''
driver = webdriver.Chrome(executable_path="C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
URL = "https://www.rahulshettyacademy.com/angularpractice/"
driver.get(URL)
driver.maximize_window()


driver.find_element_by_xpath("//*[@name='name']").send_keys("Test")
driver.find_element_by_xpath("//*[@name='email']").send_keys("xyz@xyz.com")
driver.find_element_by_xpath("//*[@id='exampleInputPassword1']").send_keys("123456")
driver.find_element_by_xpath("//*[@class='btn btn-success']").click()

'''
