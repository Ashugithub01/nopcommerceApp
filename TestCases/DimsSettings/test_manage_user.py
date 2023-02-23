import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ChooseCourt import SelectCourt
from PageObjects.SettingsOptions import Settings
from PageObjects.DimsSetting.ManageUser import Add_User
from Utilities import XLUtils

class Test_010_AddUser:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
    path = ".//TestData/DimsTestData.xlsx"

    def test_add_user(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)
        self.logger.info("--- Opening Url----")
        self.sc = SelectCourt(self.driver)
        self.sc.Enter_Email(self.email)
        self.sc.clickNext1()
        self.sc.Enter_password(self.password)
        self.sc.clickNext2()
        self.sc.demo_court()
        self.sc.adult_court()
        self.sc.proceed_next()
        self.logger.info("--- Loging Successful----")
        self.setting = Settings(self.driver)
        self.setting.Go_to_Settings()
        self.setting.Manage_User()
        actual_title = self.driver.title
        print(actual_title)
        self.adduser = Add_User(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet3')
        for r in range(2, self.rows+1):
            self.adduser.click_AddUser()
            self.driver.implicitly_wait(5)
            self.fname = XLUtils.readData(self.path, 'Sheet3', r, 1)
            self.lname = XLUtils.readData(self.path, 'Sheet3', r, 2)
            self.email = XLUtils.readData(self.path, 'Sheet3', r, 3)
            self.role = XLUtils.readData(self.path, 'Sheet3', r, 4)

            self.adduser.Enter_User_Fname(self.fname)
            self.adduser.Enter_User_Lname(self.lname)
            self.adduser.Enter_User_Email(self.email)
            self.adduser.Enter_User_Role(self.role)
            self.logger.info("--- User Details Entered----")
            self.adduser.click_Next1()
            self.adduser.attendingStaff()
            time.sleep(3)
            self.adduser.CanLogging()
            time.sleep(5)
            self.logger.info("--- Permission Allowed ----")
            self.adduser.click_Next2()
            self.adduser.Select_Court()
            self.logger.info("--- Court Access Allowed ----")
            self.adduser.click_Finish()
            time.sleep(7)
            self.logger.info(f"{self.fname + self.lname } added as new {self.role}")
            self.logger.info("*-----User Added Successfully-----*")

