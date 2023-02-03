class LoginStep1:

    textbox_email_id = "Email"
    button_Next1_xpath = "//input[@id='btnNext']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self,email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def clickNext1(self):
        self.driver.find_element_by_xpath(self.button_Next1_xpath).click()


class LoginStep2(LoginStep1):
    textbox_password_id = "Password"
    button_Next2_xpath = "//body/div[2]/div[2]/div[1]/form[1]/div[3]/div[2]/input[1]"

    firststep_linktext = "1st Judicial Demo Court"
    Secondstep_linktext = "Adult Court"
    thirdstep_xpath = "//a[@id='btnNext']"

    def Enter_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickNext2(self):
        self.driver.find_element_by_xpath(self.button_Next2_xpath).click()




