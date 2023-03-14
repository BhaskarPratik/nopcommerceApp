import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("***** SearchCustomerByName_004 ***** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info("***** Login Successfully *****")

        self.logger.info("***** Starting search customer by name *****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerManu()
        self.addcust.clickCustomerSubMenu()

        self.logger.info("***** searching customer by name *****")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName("Virat")
        searchCust.setLastName("Kohli")
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByName("Virat Kohli")
        assert True == status
        self.logger.info("***** TC_SearchCustomerByName_005 Finished *****")
        self.driver.close()