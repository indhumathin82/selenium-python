from selenium import webdriver

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getBrowserInstance(self):
        baseUrl = "https://www.amazon.com"
        if self.browser == 'ie':
            driver = webdriver.Ie(executable_path=
                                  "C:\\Users\\indhu\\pythonlast\\drivers\\IEDriverServer.exe")
        elif self.browser == 'chrome':
            driver = webdriver.Chrome(executable_path=
                                      "C:\\Users\\indhu\\pythonlast\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Firefox(executable_path=
                                       "C:\\Users\\indhu\\pythonlast\\drivers\\geckodriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
