import pytest
from PageObjects.DIMSLogin import LoginStep2
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ChooseCourt import SelectCourt
from Utilities import XLUtils


class Test_001_DimsLogin():
    baseurl = ReadConfig.getApplicationURL()
    #path = ".//TestData/DimsTestData.xlsx"
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
        self.lp = SelectCourt(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.clickNext1()
        self.lp.Enter_password(self.password)
        self.lp.clickNext2()
        self.lp.demo_court()
        self.lp.adult_court()
        self.lp.proceed_next()
        act_title = self.driver.title

        if act_title == "DIMS | Pending Screening":
            assert True
            self.logger.info("--------LoginSuccessful | Home Page ----------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginErr.png")
            self.logger.info("--------Home page title Not Verified ----------")
            self.driver.close()
            assert False

    """
    @pytest.mark.regression
    def test_DDT_login(self, setup):
        self.logger.info("*************Login Test case 001_B ************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.logger.info("------------Verifying Login --------")
        self.lp = SelectCourt(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Row",self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expect = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_Email(self.email)
            self.lp.clickNext1()
            self.lp.Enter_password(self.password)
            self.lp.clickNext2()

        act_title = self.driver.title

        if act_title == "DIMS | Pending Screening":
            if self.expect =='Pass':
                self.logger.info("--------Login Successful and Dashboard Appeared Test Passed----------")
                lst_status.append('Pass')
                print(lst_status)

            elif self.expect =='Fail':
                self.logger.info("***------Failed-----***")
                lst_status.append('Fail')

        elif act_title != "DIMS | Select Court and Docket":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginErr.png")
            if self.expect == 'Pass':
                self.logger.info("--------Login Successful and Dashboard Appeared Test Passed----------")
                lst_status.append('Fail')

            elif self.expect == 'Fail':
                self.logger.info("***------Test Passed-----***")
                lst_status.append('Pass')


        if 'Fail' not in lst_status:
            self.logger.info("___DDT Test Pass_____")
            self.driver.close()
            assert True
        else:
            self.logger.info("___DDT Test Faild____")
            self.driver.close()
            assert False
""" #DDT Login Test Case

    """ def test_clickAddParicipent(self, setup):
        self.logger.info("*************Login Test case 001_B ************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.logger.info("------------Verifying Login --------")
        self.lp = SelectCourt(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.clickNext1()
        self.lp.Enter_password(self.password)
        self.lp.clickNext2()
        self.lp.demo_court()
        self.lp.adult_court()
        self.lp.proceed_next()
        self.lp.click_Add_participent_screen()
        self.lp.discard()
        self.driver.close()
    """
