from PageObjects.DIMSLogin import LoginStep2


class SelectCourt(LoginStep2):

    firststep_linktext = "1st Judicial Demo Court"
    Secondstep_linktext = "Adult Court"
    thirdstep_xpath = "//a[@id='btnNext']"
    button_addscreen_id = "BtnAddlistScreening"
    button_discard_Rel_xpath = "//body/div[@id='listScreening']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/a[1]"

    def demo_court(self):
        self.driver.find_element_by_link_text(self.firststep_linktext).click()

    def adult_court(self):
        self.driver.find_element_by_link_text(self.Secondstep_linktext).click()

    def proceed_next(self):
        self.driver.find_element_by_xpath(self.thirdstep_xpath).click()

# -------Below function use when we add new participent -----------------------------------------------------------

    def click_Add_participent_screen(self):
        self.driver.find_element_by_id(self.button_addscreen_id).click()

    def discard(self):
        self.driver.find_element_by_xpath(self.button_discard_Rel_xpath).click()

