import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
