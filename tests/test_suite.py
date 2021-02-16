from tests.Valid_InvalidLoginTest import LoginTest
from tests.Login_SearchTest import Login_SearchTest
import unittest

ts1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
ts2 = unittest.TestLoader().loadTestsFromTestCase(Login_SearchTest)

smoketest = unittest.TestSuite([ts1,ts2])
unittest.TextTestRunner(verbosity=2).run(smoketest)