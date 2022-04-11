#Add customer page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Addcustomer:

    lnkcustomers_menu_xpath="//a[@href='#']//p[contains(text(), 'Customers')]"
    lnkcustomers_submenu_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnaddnew_xpath="//a[normalize-space()='Add new']"
    txtemail_xpath="//input[@id='Email']"
    txtpassword_xpath="//input[@id='Password']"
    txtfname_xpath="//input[@id='FirstName']"
    txtlname_xpath="//input[@id='LastName']"
    rdMalegender_id="Gender_Male"
    rdFemalegender_id="Gender_Female"
    txtdob_xpath="//input[@id='DateOfBirth']"
    txtcompanyName_id="Company"
    chkbox_isTaxexempt_id="IsTaxExempt"
    lstbox_Newsletter_id="SelectedNewsletterSubscriptionStoreIds_taglist"
    txtCustomroles_xpath="//div[@class='input-group-append input-group-required']//input[@role='listbox']"
    lstitem_administrator_xpath="//li[contains(text(),'Administrators')]"
    lstitem_forum_moderators_xpath="//li[contains(text(),'Forum Moderators')]"
   # lstitem_forum_moderators_xpath="//li[normalize-space()='Forum Moderators']"
    lstitem_Guests_xpath="//li[contains(text(),'Guests')]"
    #lstitem_Guests_xpath="// span[normalize - space() = 'Guests']"
    lstitem_Registered_xpath="//li[contains(text(),'Registered')]"
    lstitem_vendors_xpath="//li[normalize-space()='Vendors']"
   # lstitem_vendors_xpath="// li[contains(text(),'Vendors')]"
    drpManagerofvendor_xpath="//select[@id='VendorId']"
    checkBox_active_xpath="//input[@id='Active']"
    txtAdmincomment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"



    def __init__(self,driver):
        self.driver=driver
    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menu_xpath).click()

    def clickCustomersubMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_submenu_xpath).click()
    def click_addNewbutto(self):
        self.driver.find_element(By.XPATH,self.btnaddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtpassword_xpath).send_keys(password)
    def setFName(self,fname):
        self.driver.find_element(By.XPATH,self.txtfname_xpath).send_keys(fname)
    def setLName(self,lname):
        self.driver.find_element(By.XPATH,self.txtlname_xpath).send_keys(lname)
    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtdob_xpath).send_keys(dob)

    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txtCustomroles_xpath).click()
        time.sleep(13)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_administrator_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_forum_moderators_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
        time.sleep(5)
        self.listitem.click()
        #self.driver.execute_script('arguments[0].click();', self.listitem)



    def setManagerofVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpManagerofvendor_xpath))
        drp.select_by_visible_text(value)
        print(len(drp.options))
        all_options=drp.options
        for options in all_options:
            print(options.text)

    def setGender(self,gender):
        if gender =="Male":
            self.driver.find_element(By.ID,self.rdMalegender_id).click()

        elif gender=="Female":
            self.driver.find_element(By.ID,self.rdFemalegender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMalegender_id).click()

    def setCompanyname(self,compname):
        self.driver.find_element(By.ID,self.txtcompanyName_id).send_keys(compname)
    def setAdmincoment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdmincomment_xpath).send_keys(comment)
    def clicksave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()







