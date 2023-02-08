
class Settings:

    linktext_setting_xpath = "//body/nav[1]/div[1]/div[3]/ul[1]/li[2]/a[1]"

    Linktext_manageProvider_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"
    Linktext_manageUsers_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]"
    Linktext_Reports_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]"
    Linktext_Sys_Setting_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]"
    Linktext_PassReset_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]/a[1]"
    Linktext_EditUserDetails_xpath = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[7]/a[1]"

    def __init__(self, driver):
        self.driver = driver

    def Go_to_Settings(self):
        self.driver.find_element_by_xpath(self.linktext_setting_xpath).click()

    def Manage_Provider_Agency(self):
        self.driver.find_element_by_xpath(self.Linktext_manageProvider_xpath).click()

    def Manage_User(self):
        self.driver.find_element_by_xpath(self.Linktext_manageUsers_xpath).click()

    def Manage_Reports(self):
        self.driver.find_element_by_xpath(self.Linktext_Reports_xpath).click()

    def Manage_sys_setting(self):
        self.driver.find_element_by_xpath(self.Linktext_Sys_Setting_xpath).click()

    def Manage_Password_reset(self):
        self.driver.find_element_by_xpath(self.Linktext_PassReset_xpath).click()

    def Edit_User_details(self):
        self.driver.find_element_by_xpath(self.Linktext_EditUserDetails_xpath).click()
