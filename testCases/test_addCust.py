import pytest
import time
from pageObjects.LoginPage import Loginpage
from pageObjects.AddcustomerPage import Addcustomer
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_003_addCustomer:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getuserName()
    password = ReadConfig.getpassword()
    logger   = LogGen.loggg()

    def test_addCustomer(self,setup):
        self.logger.info("********Test_003_AddCustomer**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.LP=Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPwd(self.password)
        self.LP.clickLogin()

        self.logger.info("****Test***test_addCustomer Login successful***")
        self.logger.info("****started add Customer Test***")
        self.addcust=Addcustomer(self.driver)
        time.sleep(10)
        self.addcust.clickCustomerMenu()
        time.sleep(10)
        self.addcust.clickCustomersubMenu()
        time.sleep(10)
        self.addcust.click_addNewbutto()
        self.logger.info("****Providing customer information****")
        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFName("Sai")
        self.addcust.setLName("KANCHI PEERIAVA")
        self.addcust.setGender("Male")
        self.addcust.setDOB("10/10/1880")
        self.addcust.setCompanyname("IBM")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setAdmincoment("This is for testing123")
        #self.addcust.setCustomerRole("Forum Moderators")
        time.sleep(15)
        #self.addcust.setCustomerRole("Administrators")

        #self.addcust.setCustomerRole("Guests")


        self.addcust.clicksave()
        self.logger.info("****save customer details*****")
        self.logger.info("****Add customer validation starts****")


        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("***add customer Test Case is passed***")
        else:
            self.driver.save_screenshot("C:\\Users\\Arun\\PycharmProjects\\nopsaikanchi\\Screenshots\\"+"test_addCustomer_scr.png")
            assert False
            self.logger.info("***add customer Test Case is failed***")


def random_generator(size = 8, chars = string.ascii_lowercase + string.digits) :
   return ''.join(random.choice(chars) for x in range(size))


