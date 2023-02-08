import random
from Utilities.readProperties import ReadConfig
from PageObjects.ParticipentAddSanctions import AddSanction

class Test_005_AddingSanction:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    def test_add_sanction(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)

        self.asc = AddSanction(self.driver)
        self.asc.Enter_Email(self.email)
        self.asc.clickNext1()
        self.asc.Enter_password(self.password)
        self.asc.clickNext2()
        self.asc.demo_court()
        self.asc.adult_court()
        self.asc.proceed_next()

        self.asc.searchParticipent()
        self.asc.selectExistParticipent()

        self.asc.AddSaction()
        self.asc.SanctionDate()
        sanction_index = random.randint(0, 9)
        self.asc.SanctionType(sanction_index)
        self.asc.SanctionReason()
        self.asc.IsInfraction()
        self.asc.SanctionNotes()
        self.asc.SanctionTags()
        self.asc.SanctionDetailsSave()
        self.driver.close()




