import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils

import time


class Test_002_DDT_login:
    baseURL = ReadConfig.getapplicationurl()
    path = "C:\\Users\\Arun\\PycharmProjects\\nopsaikanchi\\TestData\\nop.xlsx"
    logger = LogGen.loggg()

    @pytest.mark.sanity
    def test_loginpage_DDT(self, setup):
        self.logger.info("****************** Test_002_DDT_login*****")
        self.logger.info("****************** Verifying login page*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.rows = XLUtils.getRowcount(self.path, 'Sheet1')
        self.columns = XLUtils.getColumncount(self.path, 'Sheet1')
        print("the row count is ", self.rows)
        print("the column count is", self.columns)
        Lst_status = []  # empty list variable
        for r in range(2, self.rows + 1):
            self.UserName = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.ExpectedResults = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.LP.setUserName(self.UserName)
            self.LP.setPwd(self.Password)
            self.LP.clickLogin()
            time.sleep(15)
            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if act_title == expected_title:
                if self.ExpectedResults == "Pass":
                    self.logger.info("****Passed***")
                    self.LP.clickLogout()
                    Lst_status.append("Passed")
                elif self.ExpectedResults == "Fail":
                    self.logger.info("**Failed***")
                    self.LP.clickLogout()
                    Lst_status.append("Failed")
            elif act_title != expected_title:
                if self.ExpectedResults == "Fail":
                    self.logger.info("**Passed***")
                    Lst_status.append("Passed")
                elif self.ExpectedResults == "Pass":
                    self.logger.info("***Failed***")
                    Lst_status.append("Failed")
                print(Lst_status)
        if "Failed" not in Lst_status:
            self.logger.info("***the test_login_DDT is passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("****The Test is Failed****")
            self.driver.close()
            assert False
        self.logger.info("*****Completed the  Test_002_DDT_login test***** ")
