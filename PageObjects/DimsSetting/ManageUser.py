
class Add_User:

    btn_AddUser_Xpath = "//a[@id='BtnAddNewUser']"
    inputBox_FName_id = "FirstName"
    inputBox_LName_id = "LastName"
    inputBox_UserEmail_id = "Email"
    drp_UserRole_id = "RoleId"
    btn_Next_xpath ="//input[@id='btnAddUser']"

    radio_Yes_attendStaffing_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/label[1]"
    radio_No_attendStaffing_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/label[1]"
    radio_Yes_canLogin_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/label[1]"
    radio_No_canLogin_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/label[1]"

    chkbox_court_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/label[1]"
    btn_cancel_xpath ="//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/a[1]"
    btn_Finish_xpath = "//input[@id='btnAddUser']"

    def __init__(self, driver):
        self.driver = driver

    def click_AddUser(self):
        self.driver.find_element_by_xpath(self.btn_AddUser_Xpath).click()

    def Enter_User_Fname(self,fname):
        self.driver.find_element_by_id(self.inputBox_FName_id).clear()
        self.driver.find_element_by_id(self.inputBox_FName_id).send_keys(fname)

    def Enter_User_Lname(self,lname):
        self.driver.find_element_by_id(self.inputBox_LName_id).clear()
        self.driver.find_element_by_id(self.inputBox_LName_id).send_keys(lname)

    def Enter_User_Email(self,uemail):
        self.driver.find_element_by_id(self.inputBox_UserEmail_id).clear()
        self.driver.find_element_by_id(self.inputBox_UserEmail_id).send_keys(uemail)

    def Enter_User_Role(self,urole):
        self.driver.find_element_by_id(self.drp_UserRole_id).send_keys(urole)

    def click_Next1(self):
        self.driver.find_element_by_xpath(self.btn_Next_xpath).click()

    def attendingStaff(self):
        check_Status = self.driver.find_element_by_xpath(self.radio_Yes_attendStaffing_xpath).is_selected()
        print(check_Status)
        if check_Status == True :
            pass
        elif check_Status == False:
            self.driver.find_element_by_xpath(self.radio_Yes_attendStaffing_xpath).click()

    def CanLogging(self):
        check_status = self.driver.find_element_by_xpath(self.radio_No_canLogin_xpath).is_selected()
        print(check_status)
        if check_status == True:
            self.driver.find_element_by_xpath(self.radio_Yes_canLogin_xpath).click()
        elif check_status == False:
            pass

    def click_Next2(self):
        self.driver.find_element_by_xpath(self.btn_Next_xpath).click()

    def Select_Court(self):
        stat = self.driver.find_element_by_xpath(self.chkbox_court_xpath).is_selected()
        print(stat)
        self.driver.find_element_by_xpath(self.chkbox_court_xpath).click()
        stat1 = self.driver.find_element_by_xpath(self.chkbox_court_xpath).is_selected()
        print(stat1)

    def click_Finish(self):
        self.driver.find_element_by_xpath(self.btn_Finish_xpath).click()
    """
    def click_Cancel(self):
        self.driver.find_element_by_xpath(self.btn_cancel_xpath).click()
    """