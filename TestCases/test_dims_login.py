import pytest

from PageObjects.DIMSLogin import LoginStep2
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_DimsLogin():
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************Login Test case 001_A ************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.logger.info("------------Verifying Home page title --------")

        act_title = self.driver.title

        if act_title == "DIMS | Sign in to DIMS":
            assert True
            self.logger.info("--------Home page title Verified ----------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleErr.png")
            self.logger.info("--------Home page title Not Verified ----------")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************Login Test case 001_B ************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.logger.info("------------Verifying Login --------")
        self.lp = LoginStep2(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.clickNext1()
        self.lp.Enter_password(self.password)
        self.lp.clickNext2()
        self.lp.select_demo_court()
        self.lp.select_adult_court()
        self.lp.proceed_next()
        act_title = self.driver.title

        if act_title == "DIMS | Pending Screening":
            assert True
            self.logger.info("--------Login Successful and Dashboard Appeared ----------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginErr.png")
            self.logger.info("--------Login Un-Successful ----------")
            self.driver.close()
            assert False
