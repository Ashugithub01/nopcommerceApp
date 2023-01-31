import pytest

from PageObjects.DIMSLogin import LoginStep2
from Utilities.readProperties import ReadConfig
from selenium import webdriver
from Utilities.customLogger import LogGen

class Test_001_DimsLogin():
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************Login Test case 001 ************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "DIMS | Sign in to DIMS":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleErr.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.lp = LoginStep2(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.clickNext1()
        self.lp.Enter_password(self.password)
        self.lp.clickNext2()
        self.lp.select_demo_court()
        self.lp.select_adult_court()
        self.lp.proceed_next()
        act_title = self.driver.title

        if act_title == "DIMS | Select Court and Docket":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitleErr.png")
            self.driver.close()
            assert False
