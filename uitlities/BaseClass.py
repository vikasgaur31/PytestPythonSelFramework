import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        print("Link Text is visible")

    #def selectOptionByTest(self, locator, text):
    #    sel = Select(locator)
    #    sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s, : %(levelname)s : %(name)s  : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler_object

        logger.setLevel(logging.DEBUG)

        #logger.debug('Debug statement is executed')
        return logger