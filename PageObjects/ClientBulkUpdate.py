
class Client_Bulk_update():

    navbar_bulkupdtae_xpath = "//body/nav[1]/div[1]/div[3]/ul[1]/li[3]/div[1]/i[1]"
    drp_bulkmenu_class = "//body/nav[1]/div[1]/div[3]/ul[1]/li[3]/div[1]/ul[1]"
    drplink_courtDate_xpath = "//a[contains(text(),'Bulk Update by Court Date')]"
    drplink_ClientName_xpath = "//a[contains(text(),'Bulk Update all Clients')]"
    search_clientName_xpath = "//body/div[15]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/input[1]"
    chkboc_allParticipent_id = "CheckAll"
    linktext_AddFee_id = "fee"

    def __init__(self, driver):
        self.driver = driver

    def ClickBulk_Update(self):
        self.driver.find_element_by_xpath(self.navbar_bulkupdtae_xpath).click()

    def Select_Bulk_option(self, options):

        if options == "Bulk Update by Court Date":
            self.driver.find_element_by_xpath(self.drplink_courtDate_xpath).click()
        elif options == "Bulk Update all Clients":
            self.driver.find_element_by_xpath(self.drplink_ClientName_xpath).click()

    def Search_ByclientName(self, participantName):
        self.driver.find_element_by_xpath(self.search_clientName_xpath).clear()
        self.driver.find_element_by_xpath(self.search_clientName_xpath).send_keys(participantName)

    def Search_ByInductionDate(self, InductDate):
        self.driver.find_element_by_xpath(self.search_clientName_xpath).clear()
        self.driver.find_element_by_xpath(self.search_clientName_xpath).send_keys(InductDate)

    def SelectAllCheckbox(self):

        status1 = self.driver.find_element_by_id(self.chkboc_allParticipent_id).is_enabled()
        print(status1)
        status2 = self.driver.find_element_by_id(self.chkboc_allParticipent_id).is_selected()
        print(status2)
        self.driver.find_element_by_id(self.chkboc_allParticipent_id).click()

    def AddFee_toAll(self):
        self.driver.find_element_by_id(self.linktext_AddFee_id).click()
