from base.SeleniumDriver import SeleniumDriver
import time

class Login_tests(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _signin = "nav-link-accountList-nav-line-1"
    _email = "ap_email"
    _continue = "continue"
    _password = "ap_password"
    _signinsubmit = "signInSubmit"
    _alert = "//h4[contains(text(),'There was a problem')]"
    _mousehover = "nav-link-accountList"
    _signout = "//span[contains(text(),'Sign Out')]"

    def signinclick(self):
        self.elementClick(self._signin, locatortype="id")
    def emailfield(self, email1):
        self.sendkeys(email1, self._email, locatortype="id")
    def continueclick(self):
        self.elementClick(self._continue, locatortype="id")
    def passwordfield(self, password):
        self.sendkeys(password, self._password, locatortype="id")
    def submitclick(self):
        self.elementClick(self._signinsubmit, locatortype="id")
    def alertmsgcheck(self):
        self.isElementPresent(self._alert, locatortype="xpath")
    def clearemail(self):
        self.clearfields(self._email, locatortype="id")
    def mousehoverclick(self):
        self.mousehover(self._mousehover, locatortype1="id", locator2=self._signout, locatortype2="xpath")

    def Login(self, email, password):
        self.clearemail()
        self.emailfield(email)
        self.continueclick()
        self.passwordfield(password)
        self.submitclick()
        time.sleep(3)
        # self.mousehoverclick()
    def invalidLogin(self, email):
        self.signinclick()
        self.emailfield(email)
        self.continueclick()
        self.alertmsgcheck()