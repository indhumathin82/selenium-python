from pages.LoginandSearchPage import test_Loginpage
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.data_reader import readCSV
@pytest.mark.usefixtures("oneTimeSetUp")
@ddt()
class Login_SearchTest(unittest.TestCase):
        # baseUrl = "https://www.amazon.com"
        # driver = webdriver.Firefox(executable_path=
        #                                        "C:\\Users\\indhu\\pythonlast\\drivers\\geckodriver.exe")
        # driver.get(baseUrl)
        # BP = test_Loginpage(driver)

        @pytest.fixture(autouse=True)
        def classSetup(self, oneTimeSetUp):
                self.LSP = test_Loginpage(self.driver)

        # @pytest.mark.run(order=1)
        def test_1loginpage(self):
                self.LSP.Login("indhu.narayanan@gmail.com", "pothanuri84")

        # @pytest.mark.run(order=2)
        # @data(("pepper", "1234", "indhu"),("pepper spray", "5678", "mathi"))
        @data(*readCSV("C:\\Users\\indhu\\pythonlast\\pythonProject\\Amazon\\data_file.csv"))
        @unpack
        def test_2carddetails(self, searchname, ccNum, ccName):
                self.LSP.allcarddetails(searchname, ccNum, ccName)

