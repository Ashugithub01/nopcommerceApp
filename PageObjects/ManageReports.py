
class Setting_reports:

#   ----------------------------------------------------------------------------------------------------

    linktext_ReportPrint_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"
    drp_ReportType_xpath = "//select[@id='ReportTypes']"
    drp_CourtType_xpath = "//select[@id='DIMSReportFilters_CourtId']"
    drp_DocketType_xpath = "//select[@id='DIMSReportFilters_DocketId']"
    drp_FileType_xpath = "//select[@id='ReportDocType']"
    drp_Judge_xpath = "//select[@id='DIMSReportFilters_JudgeId']"
    input_Startdate_id = "DIMSReportFilters_CourtDate"
    drp_OrderType_xpath = "//select[@id='DIMSReportFilters_drpOrderBy']"
    btn_submit_id = "btnSearch"
    link_printreport_xpath = "//a[@id='aPrint']"
#   ----------------------------------------------------------------------------------------------------

    linktext_ReportHistory_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]"
    linktext_ReportProfiling_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]"

    def __init__(self, driver):
        self.driver = driver

#  =========================================Report Printing================================================

    def GoTo_ReportPrint(self):
        self.driver.find_element_by_xpath(self.linktext_ReportPrint_xpath).click()

    def Type_of_Reports(self, Repotype):
        self.driver.find_element_by_xpath(self.drp_ReportType_xpath).send_keys(Repotype)

    def Court_type(self, Courttype):
        self.driver.find_element_by_xpath(self.drp_CourtType_xpath).send_keys(Courttype)

    def Docket_Type(self, Dockettype):
        self.driver.find_element_by_xpath(self.drp_DocketType_xpath).send_keys(Dockettype)

    def Type_of_File(self, filetype):
        try:
                if filetype == "PDF" and self.drp_ReportType_xpath == "Staff Report":
                    return self.driver.find_element_by_xpath(self.drp_FileType_xpath).send_keys(filetype)

                elif filetype == "PDF" and self.drp_ReportType_xpath != "Staff Report":
                    return self.driver.find_element_by_xpath(self.drp_FileType_xpath).send_keys(filetype)
                elif filetype == "Excel" and self.drp_ReportType_xpath != "Staff Report":
                    return self.driver.find_element_by_xpath(self.drp_FileType_xpath).send_keys(filetype)
        except NameError:
            return "NameError occurred. file type isn't defined."

    def Select_Judge(self, judgeName):
        self.driver.find_element_by_xpath(self.drp_Judge_xpath).send_keys(judgeName)

    def Select_StartDate(self, strDate):

        self.driver.find_element_by_id(self.input_Startdate_id).send_keys(strDate)

    def Type_order(self, orderType):

        self.driver.find_element_by_xpath(self.drp_OrderType_xpath).send_keys(orderType)

    def Submit_Report(self):
        self.driver.find_element_by_id(self.btn_submit_id).click()

    def Generate_Staff_report(self):
            try:
                printIcon = self.driver.find_element_by_xpath(self.link_printreport_xpath).is_enabled()
                print("Print Icon Is visible", printIcon)
                if printIcon == "True":
                    return self.driver.find_element_by_xpath(self.link_printreport_xpath).click()
                elif printIcon == "False":
                    return "error1 "
            except:
                pass





#  =========================================Report History================================================

    def GoTo_ReportHistory(self):
        self.driver.find_element_by_xpath(self.linktext_ReportHistory_xpath).click()

#  =========================================Report Profiling================================================

    def GoTo_ReportProfiling(self):
        self.driver.find_element_by_xpath(self.linktext_ReportProfiling_xpath).click()
