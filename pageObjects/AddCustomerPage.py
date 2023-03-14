import time
from telnetlib import EC

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    linkCustomer = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkSubCustomer = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddCustomer = "//a[@class='btn btn-primary']"
    txtEmail = "//input[@id='Email']"
    txtPassword = "//input[@id='Password']"
    txtFirstName = "//input[@id='FirstName']"
    txtLastName = "//input[@id='LastName']"
    rdBtnMale = "//input[@id='Gender_Male']"
    rdBtnFemale = "//input[@id='Gender_Female']"
    txtDOB = "//input[@id='DateOfBirth']"
    txtCompanyName = "//input[@id='Company']"
    chkBoxTax = "//input[@id='IsTaxExempt']"
    ddlNewsletter = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-focused " \
                    "k-state-border-down']/select[@id = 'SelectedNewsletterSubscriptionStoreIds'] "
    lstStoreName = "//span[contains(.,'Your store name')]"
    lstTestStore = "//*[@id='SelectedNewsletterSubscriptionStoreIds']/option[2]"
    lstItemAdministrator = "//span[normalize-space()='Administrators']"
    lstItemRegistered = "//span[normalize-space()='Registered']"
    lstItemVendors = "//span[normalize-space()='Vendors']"
    lstItemGuests = "//li[normalize-space()='Guests']"
    drpOfVender = "//select[@id='VendorId']"
    lstItemModerators = "//span[normalize-space()='Forum Moderators']"
    chkBtnActive = "//input[@id='Active']"
    txtAdminComment = "//textarea[@id='AdminComment']"
    btnSave = "//button[@name='save']//i[@class='far fa-save']"
    ddlCustomerRoles = "//*[@id='customer-info']/div[2]/div[11]/div[2]/div/div[1]/div/div"
    ddlVender = "//*[@id='VendorId']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerManu(self):
        self.driver.find_element("xpath", self.linkCustomer).click()

    def clickCustomerSubMenu(self):
        self.driver.find_element("xpath", self.linkSubCustomer).click()

    def clickAddCustomerBtn(self):
        self.driver.find_element("xpath", self.btnAddCustomer).click()

    def setEmail(self, email):
        self.driver.find_element("xpath", self.txtEmail).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("xpath", self.txtPassword).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element("xpath", self.txtFirstName).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element("xpath", self.txtLastName).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element("xpath", self.rdBtnMale).click()
        elif gender == "Female":
            self.driver.find_element("xpath", self.rdBtnFemale).click()
        else:
            self.driver.find_element("xpath", self.rdBtnMale).click()

    def selectDOB(self, dob):
        self.driver.find_element("xpath", self.txtDOB).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element("xpath", self.txtCompanyName).send_keys(companyName)

    def checkTax(self):
        self.driver.find_element("xpath", self.chkBoxTax).click()

    def checkActiveCheckbox(self):
        self.driver.find_element("xpath", self.chkBtnActive).click()

    def setAdminComment(self, txtAdminComment):
        self.driver.find_element("xpath", self.txtAdminComment)

    def setcustomerRoles(self, role):
        # self.driver.find_element("xpath", self.ddlCustomerRoles).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.lstItemRegistered)
        elif role == "Administrators":
            self.listitem = self.driver.find_element("xpath", self.lstItemAdministrator)

        elif role == 'Guests':
            time.sleep(3)
            button = self.driver.find_element("xpath", "//span[contains(@aria-label,'delete')]")
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
            # self.driver.find_element("xpath", self.ddlCustomerRoles).click()
            self.listitem = self.driver.find_element("xpath", self.lstItemGuests)

        elif role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.lstItemRegistered)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element("xpath", self.lstItemVendors)
        else:
            self.listitem = self.driver.find_element("xpath", self.lstItemGuests)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVender(self, value):
        drp = Select(self.driver.find_element("xpath", self.ddlVender))
        drp.select_by_visible_text(value)

    def setNewsletter(self, news):
        self.driver.find_element("xpath",
                                 "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/input").click()
        time.sleep(3)
        if news == 'Your store name':
            self.lstitem = self.driver.find_element('xpath', self.lstStoreName)
        elif news == 'Test store 2':
            self.lstitem = self.driver.find_element('xpath', self.lstTestStore)
        else:
            self.lstitem = self.driver.find_element('xpath', self.lstStoreName)
            # self.lstitem = self.driver.find_element('xpath', self.lstTestStore)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    # def setNewsletter(self, value):
    #     self.driver.find_element("xpath","//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div").click()
    #     time.sleep(5)
    #     drp = Select(self.driver.find_element("xpath", self.ddlNewsletter))
    #     drp.select_by_visible_text(value)

    def clickSaveBtn(self):
        self.driver.find_element("xpath", self.btnSave).click()
