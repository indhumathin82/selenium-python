from base.SeleniumDriver import SeleniumDriver
import time

class test_Loginpage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _signin = "nav-link-accountList-nav-line-1"
    _email = "ap_email"
    _continue = "continue"
    _password = "ap_password"
    _signinsubmit = "signInSubmit"
    _search = "twotabsearchtextbox"
    _searchbtn = "nav-search-submit-button"
    _imageselect = "//span[@data-cel-widget='MAIN-SEARCH_RESULTS-2']//a[@class='a-link-normal a-text-normal']"
    _addtocart = "add-to-cart-button"
    _checkout = "hlb-ptc-btn-native"
    _useaddress = "//input[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']"
    _addnewcard = "//span[@id='apx-add-credit-card-action-test-id']//a[contains(text(),'Add a credit or debit card')]"
    _ccnumber = "addCreditCardNumber"
    _ccname = "ppw-accountHolderName"
    _addcard = "//input[@name='ppw-widgetEvent:AddCreditCardEvent']"
    _alert = "//h4[contains(text(),'There was a problem.')]"
    _closebtn = "//button[@class=' a-button-close a-declarative']"
    _amazonlogo = "//i[@class='a-icon a-icon-logo a-block clickable-heading']"
    _returntocart = "//a[@href='https://www.amazon.com/gp/cart/view.html/ref=chk_logo_return_to_cart']"

    def signinclick(self):
        self.elementClick(self._signin, locatortype="id")
    def emailfield(self,email1):
        self.sendkeys(email1, self._email, locatortype="id")
    def continueclick(self):
        self.elementClick(self._continue, locatortype="id")
    def passwordfield(self,password):
        self.sendkeys(password,self._password, locatortype="id")
    def submitclick(self):
        self.elementClick(self._signinsubmit, locatortype="id")
    def searchfield(self,search):
        self.sendkeys(search,self._search, locatortype="id")
    def searchbtnclick(self):
        self.elementClick(self._searchbtn, locatortype="id")
    def imageclick(self):
        time.sleep(7)
        self.elementClick(self._imageselect, locatortype="xpath")
    def addtocart(self):
        self.elementClick(self._addtocart, locatortype="id")
    def checkout(self):
        self.elementClick(self._checkout, locatortype="id")
    def useaddress(self):
        self.elementClick(self._useaddress, locatortype="xpath")
    def newcard(self):
        time.sleep(3)
        self.elementClick(self._addnewcard, locatortype="xpath")
    def alertmsgcheck(self):
        print("!!!!!!!!!!!! ALERT MSG IS FOUND !!!!!!!!!!!!!!")
        self.driver.switch_to.frame("ApxSecureIframe")
        time.sleep(7)
        self.driver.find_element_by_xpath(self._alert)
    def closebtnclick(self):
        self.elementClick(self._closebtn, locatortype="xpath")
    def logobtnclick(self):
        self.driver.switch_to.default_content()
        # time.sleep(5)
        self.elementClick(self._amazonlogo, locatortype="xpath")
    def retuntocart(self):
        self.elementClick(self._returntocart, locatortype="xpath")

    def carddetails(self, ccnum, ccname):
        time.sleep(3)
        self.driver.switch_to.frame("ApxSecureIframe")
        self.sendkeys(ccnum, self._ccnumber, locatortype="name")
        self.sendkeys(ccname, self._ccname, locatortype="name")
        self.elementClick(self._addcard, locatortype="xpath")
        self.driver.switch_to.default_content()

    def Login(self, email, password):
        self.signinclick()
        self.emailfield(email)
        self.continueclick()
        self.passwordfield(password)
        self.submitclick()

    def allcarddetails(self, search, ccnum, ccname):
        self.searchfield(search)
        self.searchbtnclick()
        self.imageclick()
        self.addtocart()
        time.sleep(5)
        self.checkout()
        self.useaddress()
        time.sleep(5)
        self.newcard()
        self.carddetails(ccnum, ccname)
        self.alertmsgcheck()
        self.closebtnclick()
        self.logobtnclick()
        self.retuntocart()