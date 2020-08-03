from com.source.PageObjects.PHPTravelLoginPage import PHPTravelLoginPage


class PHPTravelLoginTest:
    def __init__(self):
        print("I am in PHP travel login test")
        self.phpTravelLoginPage = PHPTravelLoginPage()
    
    def enterURL(self, url):
        self.phpTravelLoginPage.enterURL(url)

    def goToLoginPage(self):
        self.phpTravelLoginPage.goToLoginPage()
        