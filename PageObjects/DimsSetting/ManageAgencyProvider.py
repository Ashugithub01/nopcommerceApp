
class ManageProvider:

    addAgency_linktext_xpath ="//a[contains(text(),'Add Agency/Provider')]"
    inputBox_ProviderName_id = "treatmentProvider_ProviderName"
    inputBox_ProviderEmail_id = "treatmentProvider_Email"
    inputBox_ProviderPhone_id = "treatmentProvider_Phone"
    drp_courtAgency_id = "CourtId"
    sliderround_Active_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/label[1]/span[1]"
    popup_confirm_xpath = "//button[contains(text(),'×')]"
    btn_savebtn_xpath ="//input[@id='BtnSaveTp']"

    def __init__(self, driver):
        self.driver = driver

    def Click_Add_Agency(self):
        self.driver.find_element_by_xpath(self.addAgency_linktext_xpath).click()

    def Provide_Name(self, ProviderName):
        self.driver.find_element_by_id(self.inputBox_ProviderName_id).clear()
        self.driver.find_element_by_id(self.inputBox_ProviderName_id).send_keys(ProviderName)

    def Provide_Email(self, ProvideEmail):
        self.driver.find_element_by_id(self.inputBox_ProviderEmail_id).clear()
        self.driver.find_element_by_id(self.inputBox_ProviderEmail_id).send_keys(ProvideEmail)

    def Provide_Phone(self, ProvidePhone):
        self.driver.find_element_by_id(self.inputBox_ProviderPhone_id).clear()
        self.driver.find_element_by_id(self.inputBox_ProviderPhone_id).send_keys(ProvidePhone)

    def Provide_Associate_Agency(self, countName):
        self.driver.find_element_by_id(self.drp_courtAgency_id).send_keys(countName)

    def Click_Active_InActive(self):

        status = self.driver.find_element_by_xpath(self.sliderround_Active_xpath).is_enabled()
        print(status)
        if status == True:
            self.driver.find_element_by_xpath(self.sliderround_Active_xpath).click()
            cnf_popup = self.driver.find_element_by_xpath(self.popup_confirm_xpath).is_enabled()
            if cnf_popup == True:
                self.driver.find_element_by_xpath(self.popup_confirm_xpath).click()
            else:
                pass
        else:
            pass

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.btn_savebtn_xpath).click()


