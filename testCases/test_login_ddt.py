import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen
from utilities import ExcelUtils


class TestLoginDDT002:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************ TestLoginDDT002 *****************")
        self.logger.info("************ Verifying login_DDT tests *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel", self.rows)

        lst_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            self.username = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLoginBtn()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("******* Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("******* Failed *****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****** Failed ******")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("****** Passed ******")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info(" ****** Login DDT Test Passed....******")
            self.driver.close()
            assert True
        else:
            self.logger.info(" ****** Login DDT Test Failed....******")
            self.driver.close()
            assert False

        self.logger.info(" ****** End of Login DDT Test ....******")
        self.logger.info(" ****** Completed TestLoginDDT002....******")