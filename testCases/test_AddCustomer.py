import random
import string
import time
import pytest

from utilities.CustomLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer


class Test_003_AddCustomer:
    basURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********** Test_03_AddCustomer ********")
        self.driver = setup
        self.driver.get(self.basURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info("***** Login Successful *****")
        self.logger.info("***** Starting Add Customer Test *****")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomerManu()
        self.addCust.clickCustomerSubMenu()
        self.addCust.clickAddCustomerBtn()

        self.logger.info("***** Providing customer info *****")
        time.sleep(5)
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Pratik")
        self.addCust.setLastName("Bhaskar")
        self.addCust.setGender("Male")
        self.addCust.selectDOB("10/28/1996")
        self.addCust.setCompanyName("BusyQA")
        self.addCust.checkTax()
        self.addCust.setNewsletter("Test store 2")
        self.addCust.setcustomerRoles("Guests")
        self.addCust.setManagerOfVender("Vendor 2")
        self.addCust.checkActiveCheckbox()
        self.addCust.setAdminComment("This is for testing")
        self.addCust.clickSaveBtn()
        self.logger.info("***** Saving Customer info")
        self.msg = self.driver.find_element("xpath", "/html/body/div[3]/div[1]/div[1]").text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info(" ***** Add customer test passed ****** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"  "test_addCustomer_src.png")
            self.logger.error("***** Add customer test failed *****")
            assert True == False
            self.driver.close()
            self.logger.info("***** Ending test_addCustomer case *****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
