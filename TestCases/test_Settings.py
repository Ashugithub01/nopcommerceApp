
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ChooseCourt import SelectCourt
from PageObjects.SettingsOptions import Settings


class Test_007_SettingOptions:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_SettingPagetitle(self, setup):
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

        self.setting = Settings(self.driver)
        self.setting.Go_to_Settings()
        actual_title = self.driver.title
        if actual_title == "DIMS | Manage Users":
            assert True
            self.logger.info("--- Setting Page title verified----")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "SettingPageTitle.png")
            self.logger.info("--- Setting Page title Failed----")
            self.driver.close()
            assert False



