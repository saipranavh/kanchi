
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class SearchCustomer:#add customer Page

    txt_email_id="SearchEmail"
    txt_fname_id="SearchFirstName"
    txt_lname_id="SearchLastName"
    btn_search_id="search-customers"
    tble_searchResults_xpath= "//div[@id='customers-grid_wrapper']//div[@class='row']"
    tble_xpath="//table[@id='customers-grid']"
    tble_row_xpath="//*[@id='customers-grid']//tbody/tr"
    tble_column_xpath = "//*[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).clear()
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)
    def setFname(self,fname):
        self.driver.find_element(By.ID,self.txt_fname_id).clear()
        self.driver.find_element(By.ID,self.txt_fname_id).send_keys(fname)
    def setLname(self,lname):
        self.driver.find_element(By.ID,self.txt_lname_id).clear()
        self.driver.find_element(By.ID,self.txt_lname_id).send_keys(lname)
    def getNoRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tble_row_xpath))
    def getNoColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tble_column_xpath))
    def clickSearch(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def searchcustemail(self,email):
        flag=False
        for r in range(1,self.getNoRows()+1):
            tbl=self.driver.find_element(By.XPATH,self.tble_xpath)
            emailid=tbl.find_element_by_xpath("//*[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag=True
                break
        return flag

    def search_custByName(self,name):
        flag=False
        for r in range(1,self.getNoRows()+1):
            tbl=self.driver.find_element(By.XPATH,self.tble_xpath)
            Name=tbl.find_element_by_xpath("//*[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
        return flag




