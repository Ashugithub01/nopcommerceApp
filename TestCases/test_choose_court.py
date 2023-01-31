from PageObjects.DIMSLogin import LoginStep2
from PageObjects.AddScreening import PatientAddScreen
from Utilities.readProperties import ReadConfig

class Test_002_ChooseCourtName():

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    def test_choosecourt(self, setup):
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
        self.cp.add_screen()
        self.cp.discard()
        self.driver.close()





