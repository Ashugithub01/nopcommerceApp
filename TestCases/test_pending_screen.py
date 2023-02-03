import pytest
from PageObjects.ChooseCourt import SelectCourt
from Utilities.readProperties import ReadConfig
from PageObjects.PendingScreening import PendingScreen
from PageObjects.DIMSLogin import LoginStep2,LoginStep1

class Test_004_PendingScreen:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password =ReadConfig.getpassword()

    @pytest.mark.sanity
    #@pytest.mark.regression
    def test_PendingScreen_title(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)

        self.Ls1 = LoginStep1(self.driver)
        self.Ls1.Enter_Email(self.email)
        self.Ls1.clickNext1()

        self.sc = SelectCourt(self.driver)
        self.sc.Enter_password(self.password)
        self.sc.clickNext2()
        self.sc.demo_court()
        self.sc.adult_court()
        self.sc.proceed_next()

        self.ps = PendingScreen(self.driver)
        self.ps.pendingSceen_tab()
        act_title = self.driver.title
        if act_title == "DIMS | Pending Screening":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "PendingScreenTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_participent(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)

        self.Ls1 = LoginStep1(self.driver)
        self.Ls1.Enter_Email(self.email)
        self.Ls1.clickNext1()

        self.sc = SelectCourt(self.driver)
        self.sc.Enter_password(self.password)
        self.sc.clickNext2()
        self.sc.demo_court()
        self.sc.adult_court()
        self.sc.proceed_next()

        ps = PendingScreen(self.driver)
        ps.pendingSceen_tab()
        ps.seatch_parti("leona")
#       status = ps.serch_by_name("leona")
#       assert True==status
        self.driver.close()

    def test_searchEdit_participent(self):
        pass

    def test_searchDel_participent(self):
        pass

