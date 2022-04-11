import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_login:
    baseURL=ReadConfig.getapplicationurl()
    username=ReadConfig.getuserName()
    password=ReadConfig.getpassword()
    logger = LogGen.loggg()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage(self,setup):
        self.logger.info("Test_001_login")
        self.logger.info("******************verifying home page title   *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

        act_title= self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** home page title test is passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage.png")
            self.driver.save_screenshot()
            self.driver.close()
            self.logger.error("****************** home page title test is failed*****")
            assert False

    def test_loginpage(self,setup):
        self.logger.info("****************** Verifying login page*****")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.LP=Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPwd(self.password)
        self.LP.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************** hai sathish Login  page title test is passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginpage.png")
            self.driver.close()
            self.logger.error("****************** Login  page title test is failed ****")
            assert False







    """
    def test_homepage_title(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title== "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP=Loginpage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPwd(self.password)
        self.LP.clickLogin()
        actl_title = self.driver.title
        if actl_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
        self.driver.close()

"""


