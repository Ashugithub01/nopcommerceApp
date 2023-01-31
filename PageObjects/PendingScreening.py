class PendingScreen:
# -----pending screen Tab---
    tab_PendingsScrenn_xpath = "//body/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"

# -----screen participent---
    Srchbar_pedingsceen_cssSel = "div.container:nth-child(12) div.col-sm-12 div.form-group div.tab-content div.tab-pane.active:nth-child(1) div.row div.col-sm-12 div.dataTables_wrapper.form-inline.dt-bootstrap.no-footer div.row:nth-child(1) div.col-sm-6:nth-child(2) div.dataTables_filter label:nth-child(2) > input.form-control.input-sm"
    table_xpath = "//table[@id='tablePending']"
    tableRows_xpath = "//table[@id='tablePending']//tbody/tr"
    tableColumns_xpath = "//table[@id='tablePending']//tbody/tr/td"
    reject_link =" //tbody/tr[1]/td[4]/a[1]"
# -----screen Edit participent---

# -----screen Del participent---


    def __init__(self, driver):
        self.driver= driver

    def pendingSceen_tab(self):
        self.driver.find_element_by_xpath(self.tab_PendingsScrenn_xpath).click()

    def seatch_parti(self, participentName):
        self.driver.find_element_by_css_selector(self.Srchbar_pedingsceen_cssSel).send_keys(participentName)

    def getNoOfRows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoOfCoulmns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    def serch_by_name(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            pname = table.find_element_by_xpath(("//table[@id='tablePending'] //tbody/tr["+str(r)+"]/td[2] ").text)
            if pname == Name:
                break
        return  flag

