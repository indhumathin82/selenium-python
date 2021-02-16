from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class testme():
    def testmethod(self):
        driver = webdriver.Firefox(executable_path=
                                           "C:\\Users\\indhu\\pythonlast\\drivers\\geckodriver.exe")
        driver.get("https://www.amazon.com")
        element = driver.find_element_by_id("nav-link-accountList")
        signout = driver.find_element_by_xpath("//span[contains(text(),'Orders')]")
        action = ActionChains(driver)
        action.move_to_element(element).move_to_element(signout).click().perform()
        # time.sleep(4)

TM = testme()
TM.testmethod()
