from PageObjects.ChooseCourt import SelectCourt
from selenium.webdriver.support.ui import Select
class AddSanction(SelectCourt):

    btn_AddSanction_xpath = "//a[contains(text(),'Add Sanction')]"
    datepick_DateSanctioned_id = "txtDate"
    dropd_Sanction_Type_xpath = "//select[@id='Type']"
    inputbox_SanctionReason_id = "txtReason"
    chkbox_infraction_id = "chkIsInfraction"
    iframe_Notes_id = ""
    search_tag_id = ""
    btn_save_id ="btnSubmit"

    def searchParticipent(self):
        pass

    def selectExistParticipent(self):
        pass

    def AddSaction(self):
        self.driver.find_element_by_xpath(self.btn_AddSanction_xpath).click()

    def SanctionDate(self, sanction_date):
        self.driver.find_element_by_id(self.datepick_DateSanctioned_id).send_keys(sanction_date)

    def SanctionType(self, sanction_type):
        sanc_type = self.driver.find_element_by_xpath(self.dropd_Sanction_Type_xpath)
        san_tp = Select(sanc_type)
        san_tp.select_by_index(sanction_type)

    def SanctionReason(self, sanction_reason):
        self.driver.find_element_by_id(self.inputbox_SanctionReason_id).send_keys(sanction_reason)

    def IsInfraction(self):
        self.driver.find_element_by_id(self.chkbox_infraction_id).click()

    def SanctionNotes(self, sanction_notes):
        pass

    def SanctionTags(self, sanction_tag):
        pass

    def SanctionDetailsSave(self):
        self.driver.find_element_by_id(self.btn_save_id).click()

    def SanctionDetailsCancel(self):
        self.driver.find_element_by_id().click()







