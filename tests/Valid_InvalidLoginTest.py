import unittest
from pages.Valid_InvalidLoginPage import Login_tests
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.LP = Login_tests(self.driver)

    # baseUrl = "https://www.amazon.com"
    # driver = webdriver.Firefox(executable_path=
    #                            "C:\\Users\\indhu\\pythonlast\\drivers\\geckodriver.exe")
    # driver.get(baseUrl)
    # BPL = Login_tests(driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.LP.invalidLogin("indhu.naranan@gmail.com")
    @pytest.mark.run(order=2)
    def test_validlogin(self):
        self.LP.Login("indhu.narayanan@gmail.com", "pothanuri84")
