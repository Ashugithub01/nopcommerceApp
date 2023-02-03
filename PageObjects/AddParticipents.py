import random
from selenium.webdriver.support.ui import Select

class AddAPrticipent:

    drpd_SelectJudge_id = "JudgeId"
    Inputbox_CaseDocket_id = "CaseDocketNumber"
    drpd_addmissionType_xpath = "//select[@id='AdmissionType']"
    drpd_realetedCourtParticipent_id = "OfferRelatedtoCourtParticipation"
    date_ReferralDate_id = "ReferralDate"
    drpd_RefferalSourece_id = "ReferralSource"
    inputbox_RefferalName_id = "ReferralName"
    inputbox_ParticpemtFName_id = "FirstName"
    inputbox_ParticpemtLName_id = "LastName"
    inputbox_SocialSecurityNo_id = "SocialSecurity"
    date_DateOfbirth_id = "DOB"
    rd_haveDL_xpath = "//body/div[@id='listScreening']/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[5]/div[10]/div[1]/div[1]/div[1]/label[1]"
    rd_haveNo_DL_xpath = "//body/div[@id='listScreening']/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[5]/div[10]/div[1]/div[1]/div[2]/label[1]"
    btn_SaveNext_id = "btnSubmit"

    def __init__(self, driver):
        self.driver= driver

    def Select_Judge(self, judageName):
        #self.driver.find_element_by_id(self.drpd_SelectJudge_id).send_keys(judageName)
        judge_drp = self.driver.find_element_by_id(self.drpd_SelectJudge_id)
        drp1 = Select(judge_drp)
        drp1.select_by_index(judageName)

    def Case_Docket_No(self, DocketNo):
        self.driver.find_element_by_id(self.Inputbox_CaseDocket_id).send_keys(DocketNo)

    def Add_addmission_type(self, Addmissiontype):
        #self.driver.find_element_by_xpath(self.drpd_addmissionType_xpath).send_keys(Addmissiontype)
        drp_element = self.driver.find_element_by_xpath(self.drpd_addmissionType_xpath)
        drp2 = Select(drp_element)
        drp2.select_by_index(Addmissiontype)

    def offer_related_court(self, relCourt):
        #self.driver.find_element_by_id(self.drpd_realetedCourtParticipent_id).send_keys(relCourt)
        offer_rel_court = self.driver.find_element_by_id(self.drpd_realetedCourtParticipent_id)
        drp3 = Select(offer_rel_court)
        drp3.select_by_index(relCourt)

    def Date_of_refferal(self, refferedDate):
        self.driver.find_element_by_id(self.date_ReferralDate_id).send_keys(refferedDate)

    def Refered_source_name(self, referedSource):
        #self.driver.find_element_by_id(self.drpd_RefferalSourece_id).send_keys(referedSource)
        ref_source_name = self.driver.find_element_by_id(self.drpd_RefferalSourece_id)
        drp4 = Select(ref_source_name)
        drp4.select_by_index(referedSource)

    def Referral_Paerson_name(self, refferalname):
        self.driver.find_element_by_id(self.inputbox_RefferalName_id).send_keys(refferalname)

    def Participent_Fname(self, Fname):
        self.driver.find_element_by_id(self.inputbox_ParticpemtFName_id).send_keys(Fname)

    def Participent_Lname(self, Lname):
        self.driver.find_element_by_id(self.inputbox_ParticpemtLName_id).send_keys(Lname)

    def social_secu_num(self, securityNum):
        self.driver.find_element_by_id(self.inputbox_SocialSecurityNo_id).send_keys(securityNum)

    def Date_of_birth(self, dob):
        self.driver.find_element_by_id(self.date_DateOfbirth_id).send_keys(dob)

    def have_driver_license(self,DriverLicense):
        if DriverLicense == "Yes":
            self.driver.find_element_by_xpath(self.rd_haveDL_xpath).click()
        elif DriverLicense == "No":
            self.driver.find_element_by_xpath(self.rd_haveNo_DL_xpath).click()

    def save_participent(self):
        self.driver.find_element_by_id(self.btn_SaveNext_id).click()




