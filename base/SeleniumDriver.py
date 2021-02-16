from selenium.webdriver.common.by import By
import utilities.CustomLogger as cl
import logging
from selenium.webdriver import ActionChains

class SeleniumDriver():

    log = cl.Custom_Logger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatortype):
        if locatortype == 'id':
            return By.ID
        elif locatortype == 'name':
            return By.NAME
        elif locatortype == 'xpath':
            return By.XPATH
        elif locatortype == 'class':
            return By.CLASS_NAME
        elif locatortype == "tag_name":
            return By.TAG_NAME
        elif locatortype == 'css_selector':
            return By.CSS_SELECTOR
        elif locatortype == 'link_text':
            return By.LINK_TEXT
        else:
            self.log.info("Not Supported locator")
        return False

    def getElement(self,locator,locatortype):
        try:
            byType = self.getByType(locatortype)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found  " + locator +" and the locator type is " + locatortype)
            return element
        except:
            self.log.info("Element not found " + locator)

    def elementClick(self, locator, locatortype):
        element = self.getElement(locator,locatortype)
        element.click()

    def sendkeys(self, data, locator, locatortype):
        element = self.getElement(locator,locatortype)
        element.send_keys(data)

    def isElementPresent(self, locator, locatortype):
        element = self.getElement(locator,locatortype)
        if element is not None:
            self.log.info("Element is present in the screen " + locator)
            return True
        else:
            self.log.info("Element is not present in the screen " + locator)
            return False

    def clearfields(self, locator, locatortype):
        element = self.getElement(locator,locatortype)
        element.clear()

    def mousehover(self, locator1, locatortype1, locator2, locatortype2):
        element1 = self.getElement(locator1, locatortype1)
        element2 = self.getElement(locator2, locatortype2)
        action = ActionChains(self.driver)
        action.move_to_element(element1).move_to_element(element2).click().perform()
