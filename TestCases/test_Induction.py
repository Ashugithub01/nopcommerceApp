import datetime
from Utilities.readProperties import ReadConfig


class Test_005_InductionDetails:

    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    def test_inductionFillign(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)


        current_date = datetime.date.today()
