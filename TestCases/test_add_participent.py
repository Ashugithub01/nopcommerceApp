import time

import pytest

from Utilities.readProperties import ReadConfig
from PageObjects.AddScreening import PatientAddScreen
from PageObjects.AddParticipents import AddAPrticipent
from Utilities.customLogger import LogGen

class Test_003_Addnew_participents:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_participent(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.logger.info("*************Test_003_Addnew_participents ************")
        self.driver.get(self.baseurl)
        self.logger.info("--- Launching URL ---")
        self.cp = PatientAddScreen(self.driver)
        self.logger.info("--- Enter Credential ---")
        self.cp.Enter_Email(self.email)
        self.cp.clickNext1()
        self.cp.Enter_password(self.password)
        self.cp.clickNext2()
        self.logger.info("--- Login Successful---")
        self.logger.info("--- Choosing Court---")
        self.cp.demo_court()
        self.cp.adult_court()
        self.cp.proceed_next()
        self.logger.info("--- Adding New Participent---")
#-----------------------------------------------------------------------------

        self.cp.add_screen()
        time.sleep(3)
        self.ap = AddAPrticipent(self.driver)

        self.ap.Select_Judge("Clara Ramirez")
        self.ap.Case_Docket_No('764874')
        self.ap.Add_addmission_type("Abuse-Neglect")
        self.ap.offer_related_court("Case Dismissal")
        self.ap.Date_of_refferal("01/29/2023")
        self.ap.Refered_source_name("Prosecutor")
        self.ap.Referral_Paerson_name("Emili blaire")
        self.ap.Participent_Fname("Kate")
        self.ap.Participent_Lname("Walter")
        self.ap.social_secu_num("000-00-0104")
        self.ap.Date_of_birth("01/28/1994")
        self.ap.have_driver_license("No")

        self.ap.save_participent()
        time.sleep(20)

        act_title = self.driver.title
        if act_title == "DIMS | Induction":
            assert True
            self.logger.info("--- Participent Added Successful---")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Add_New_Participent.png")
            self.logger.info("--- Participent Adding Failed ---")
            self.driver.close()
            assert False












