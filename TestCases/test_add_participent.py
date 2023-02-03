import random
import time
import pytest
from Utilities.readProperties import ReadConfig
from PageObjects.ChooseCourt import SelectCourt
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
        self.driver.implicitly_wait(10)
        self.logger.info("*************Test_003_Addnew_participents ************")
        self.driver.get(self.baseurl)
        self.logger.info("--- Launching URL ---")
        self.cp = SelectCourt(self.driver)
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

        self.cp.click_Add_participent_screen()
        time.sleep(3)
        self.ap = AddAPrticipent(self.driver)

        judgename_idex= random.randint(1, 9)
        self.ap.Select_Judge(judgename_idex)
        time.sleep(5)

        csr = random.randint(10001, 99999)
        self.ap.Case_Docket_No(csr)
        time.sleep(5)

        admisson_type_index = random.randint(0, 9)
        self.ap.Add_addmission_type(admisson_type_index)
        time.sleep(5)

        offerRel_court_index = random.randint(0, 11)
        self.ap.offer_related_court(offerRel_court_index)
        time.sleep(5)

        self.ap.Date_of_refferal("01/29/2023")
        time.sleep(2)

        Ref_sourcename_index = random.randint(0, 8)
        self.ap.Refered_source_name(Ref_sourcename_index)
        time.sleep(5)

        self.ap.Referral_Paerson_name("Emili willis")
        self.ap.Participent_Fname("Luis")
        self.ap.Participent_Lname("Frazier")

        sec_no = random.randint(100011111, 999999999)
        self.ap.social_secu_num(sec_no)
        time.sleep(5)

        self.ap.Date_of_birth("01/28/1994")
        time.sleep(2)
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












