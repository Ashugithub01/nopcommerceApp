from datetime import date
import time
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.ClientBulkUpdate import Client_Bulk_update
from PageObjects.ChooseCourt import SelectCourt

class Test_006_clientbulkUpdate:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
    """
    def test_verifying_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)

        self.sc = SelectCourt(self.driver)
        self.sc.Enter_Email(self.email)
        self.sc.clickNext1()
        self.sc.Enter_password(self.password)
        self.sc.clickNext2()
        self.sc.demo_court()
        self.sc.adult_court()
        self.sc.proceed_next()
        self.logger.info("----------Click on Bulk Option from Nav Bar--------")
        self.cbulk2 = Client_Bulk_update(self.driver)
        self.cbulk2.ClickBulk_Update()
        time.sleep(4)
        self.logger.info("----------Selecting Bulk Update option--------")
        self.cbulk2.Select_Bulk_option("Bulk Update all Clients")
        #self.cbulk2.Select_Bulk_option("Bulk Update by Court Date")

        acttul_title = self.driver.title
        self.logger.info("----------Verifying title Page--------")
        if acttul_title == "DIMS | Bulk Update AllClients":
            assert True
            self.logger.info("----------Page Verification Successful--------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "BulkUpdateByClient.png")
            self.logger.info("----------Page Verification Failed--------")
            self.driver.close()
            assert False
    """
    def test_SearchByName(self):
        pass

    def test_SearchBy_InductionDate(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)

        self.sc = SelectCourt(self.driver)
        self.sc.Enter_Email(self.email)
        self.sc.clickNext1()
        self.sc.Enter_password(self.password)
        self.sc.clickNext2()
        self.sc.demo_court()
        self.sc.adult_court()
        self.sc.proceed_next()
        self.logger.info("----------Click on Bulk Option from Nav Bar--------")
        self.cbulk2 = Client_Bulk_update(self.driver)
        self.cbulk2.ClickBulk_Update()
        time.sleep(4)
        self.logger.info("----------Selecting Bulk Update option--------")
        self.cbulk2.Select_Bulk_option("Bulk Update all Clients")

        today = date.today()
        current_date = today.strftime("%m/%d/%Y")
        self.cbulk2.Search_ByInductionDate(str(current_date))
        self.cbulk2.SelectAllCheckbox()
        time.sleep(5)

        self.cbulk2.AddFee_toAll()


