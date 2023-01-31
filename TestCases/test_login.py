import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleErr.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitleErr.png")
            self.driver.close()
            assert False