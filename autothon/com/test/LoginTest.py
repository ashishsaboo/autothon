from com.source.PageObjects.LoginPage import LoginPage

class LoginTest:
    def __init__(self):
        self.loginPage = LoginPage()
    
    def loginToApplication(self):
        self.loginPage.executeTest()
        
        