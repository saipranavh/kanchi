

import pytest
import time
from pageObjects.LoginPage import Loginpage
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.searchCust import SearchCustomer
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig

class Test_005_searchCustbyName:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getuserName()
    password = ReadConfig.getpassword()
    logger = LogGen.loggg()  # logger
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_byName(self,setup):
        self.logger.info("*****Test_005_searchCustbyName****")
        self.logger.info("*********search _customer_by _Name_005*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.LP=Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPwd(self.password)
        self.LP.clickLogin()
        self.logger.info("*********Login successful*********")
        self.logger.info("****start Add customer****")
        self.AddCust=Addcustomer(self.driver)
        self.AddCust.clickCustomerMenu()
        self.AddCust.clickCustomersubMenu()
        self.AddCust.click_addNewbutto()
        time.sleep(5)
        self.AddCust.setEmail("ksaiindia12@gmail.com")
        self.AddCust.setFName("sai")
        self.AddCust.setLName("ram")
        self.AddCust.setCompanyname("IBM")
        self.AddCust.setManagerofVendor("Vendor 2")
        self.AddCust.setAdmincoment("This is for testing123")
        self.AddCust.setCustomerRole("Forum Moderators")
        self.AddCust.clicksave()
        time.sleep(15)
        self.SbyName=SearchCustomer(self.driver)
        self.SbyName.setFname("sai")
        self.SbyName.clickSearch()
        status=self.SbyName.search_custByName("sai ram")
        assert True==status
        self.logger.info("The tc search by name is pass")

