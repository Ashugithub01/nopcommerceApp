import time
from datetime import date
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ChooseCourt import SelectCourt
from PageObjects.SettingsOptions import Settings
from PageObjects.DimsSetting.ManageAgencyProvider import ManageProvider
from Utilities import XLUtils

class Test_009_AddAgencyProvider:

    baseurl = ReadConfig.getApplicationURL()
    path = ".//TestData/DimsTestData.xlsx"
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_verifyTitle(self,setup):
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
        self.setting.Manage_Provider_Agency()
        actual_title = self.driver.title
        print(actual_title)

        self.add_provider = ManageProvider(self.driver)

        time.sleep(3)

        self.rows = XLUtils.getRowCount(self.path,'AgencyProvider')
        lst_status = []
        for r in range(2, self.rows+1):
            self.add_provider.Click_Add_Agency()
            self.pName = XLUtils.readData(self.path, 'AgencyProvider', r, 1)
            self.pEMail = XLUtils.readData(self.path, 'AgencyProvider', r, 2)
            self.pPhone = XLUtils.readData(self.path, 'AgencyProvider', r, 3)
            self.pCourt = XLUtils.readData(self.path, 'AgencyProvider', r, 4)
            self.expect = XLUtils.readData(self.path, 'AgencyProvider', r, 5)

            self.add_provider.Provide_Name(self.pName)
            self.add_provider.Provide_Email(self.pEMail)
            self.add_provider.Provide_Phone(self.pPhone)
            self.add_provider.Provide_Associate_Agency(self.pCourt)
            self.add_provider.Click_Active_InActive()
            time.sleep(2)
            self.add_provider.Click_Save()
            time.sleep(7)
            # self.driver.close()




