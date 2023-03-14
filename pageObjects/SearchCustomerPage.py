class SearchCustomer:
    txtEmail = "//input[@id='SearchEmail']"
    txtFirstName = "//input[@id='SearchFirstName']"
    txtLastName = "//input[@id='SearchLastName']"
    btnSearch = "//button[@id='search-customers']"
    tableSearchResult = "//table[@id='customers-grid']"
    tableXpath = "//table[@id='customers-grid']"
    tableRowsXpath = "//table[@id='customers-grid']/tbody/tr"
    tableColumnsXpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element("xpath", self.txtEmail).clear()
        self.driver.find_element("xpath", self.txtEmail).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element("xpath", self.txtFirstName).clear()
        self.driver.find_element("xpath", self.txtFirstName).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element('xpath', self.txtLastName).clear()
        self.driver.find_element('xpath', self.txtLastName).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element('xpath', self.btnSearch).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements('xpath', self.tableRowsXpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements("xpath", self.tableColumnsXpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element('xpath', self.tableXpath)
            emailId = table.find_element('xpath', '//table[@id="customers-grid"]/tbody/tr["+ str(r)+"]/td[2]').text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element('xpath', self.tableXpath)
            name = table.find_element('xpath', '//table[@id="customers-grid"]/tbody/tr["+ str(r)+"]/td[3]').text
            if name == Name:
                flag = True
                break
        return flag
