import time
from datetime import date
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ChooseCourt import SelectCourt
from PageObjects.SettingsOptions import Settings
from PageObjects.ManageReports import Setting_reports


class Test_008_SettingReports:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_ReportPrint(self, setup):
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
        self.setting.Manage_Reports()
        actual_title = self.driver.title
        if actual_title == "DIMS | Reports":
            assert True
            self.logger.info("--- Setting Page title verified----")
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "SettingPageTitle.png")
            self.logger.info("------ Page title Failed----")
            #self.driver.close()
            assert False

        self.setRepo = Setting_reports(self.driver)
        self.setRepo.GoTo_ReportPrint()
        self.setRepo.Type_of_Reports("Staff Report") #--Docket Profile
        time.sleep(3)
        self.setRepo.Court_type("1st Judicial Demo Court")
        time.sleep(3)
        self.setRepo.Docket_Type("Adult Court")
        time.sleep(3)
        self.setRepo.Type_of_File("PDF")
        time.sleep(3)
        self.setRepo.Select_Judge("Any")
        time.sleep(3)
        """ 
        today = date.today()
        current_date = today.strftime("%m/%d/%Y")
        """
        self.setRepo.Select_StartDate("02/01/2023")
        time.sleep(3)
        self.setRepo.Type_order("Ascending by Name")
        self.setRepo.Submit_Report()
        self.setRepo.Generate_Staff_report()
        self.driver.close()




