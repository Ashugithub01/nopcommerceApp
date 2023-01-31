import time

import pytest

from Utilities.readProperties import ReadConfig
from PageObjects.AddScreening import PatientAddScreen
from PageObjects.AddParticipents import AddAPrticipent

class Test_003_Addnew_participents:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_participent(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseurl)
        self.cp = PatientAddScreen(self.driver)
        self.cp.Enter_Email(self.email)
        self.cp.clickNext1()
        self.cp.Enter_password(self.password)
        self.cp.clickNext2()
        self.cp.demo_court()
        self.cp.adult_court()
        self.cp.proceed_next()

#-----------------------------------------------------------------------------

        self.cp.add_screen()
        self.ap = AddAPrticipent(self.driver)

        self.ap.Select_Judge("Clara Ramirez")
        self.ap.Case_Docket_No('764873')
        self.ap.Add_addmission_type("Abuse-Neglect")
        self.ap.offer_related_court("Case Dismissal")
        self.ap.Date_of_refferal("01/29/2023")
        self.ap.Refered_source_name("Prosecutor")
        self.ap.Referral_Paerson_name("Emili blaire")
        self.ap.Participent_Fname("Hilary")
        self.ap.Participent_Lname("Duff")
        self.ap.social_secu_num("000-00-0103")
        self.ap.Date_of_birth("01/28/1994")
        self.ap.have_driver_license("No")

        self.ap.save_participent()
        time.sleep(20)

        act_title = self.driver.title
        if act_title == "DIMS | Induction":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Add_New_Participent.png")
            self.driver.close()
            assert False












