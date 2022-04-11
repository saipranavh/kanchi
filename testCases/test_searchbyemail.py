import time
import pytest
from pageObjects.LoginPage import Loginpage
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.searchCust import SearchCustomer
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig

class Test_004_searchCust_byEmail:
    baseURL=ReadConfig.getapplicationurl()
    username=ReadConfig.getuserName()
    password=ReadConfig.getpassword()
    logger=LogGen.loggg()#logger

    def test_search_by_email(self,setup):
        self.logger.info("*********search _customer_by _email_004*********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.LP=Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPwd(self.password)
        self.LP.clickLogin()
        self.addcust=Addcustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomersubMenu()
        self.addcust.click_addNewbutto()
        self.addcust.setEmail("ksaik0@gmail.com")
        self.addcust.setCompanyname("IBM")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setAdmincoment("This is for testing123")
        self.addcust.setCustomerRole("Forum Moderators")
        time.sleep(15)
        #self.addcust.setCustomerRole("Administrators")

        # self.addcust.setCustomerRole("Guests")

        self.addcust.clicksave()
        self.logger.info("*********search customer by email******")
        sEmail=SearchCustomer(self.driver)
        sEmail.getNoRows()
        sEmail.getNoColumns()
        time.sleep(10)
        sEmail.setEmail("ksaik0@gmail.com")
        sEmail.clickSearch()
        time.sleep(4)
        status=sEmail.searchcustemail("ksaik0@gmail.com")
        #assert status is True
        assert True==status
        self.logger.info("the tc search by email  is pass")



