import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('UAT common info', 'baseurl')
        return url

    @staticmethod
    def getemail():
        email = config.get('UAT common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('UAT common info', 'password')
        return password
