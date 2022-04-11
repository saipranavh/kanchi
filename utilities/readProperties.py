import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\Arun\\PycharmProjects\\nopsaikanchi\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url= config.get('common info','baseurl')
        return url

    @staticmethod
    def getuserName():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password
