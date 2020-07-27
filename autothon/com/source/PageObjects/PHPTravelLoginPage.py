from com.source.driver.DriverInit import WebDriver

class PHPTravelLoginPage:
    def __init__(self):
        print("I am in PHP travel login page")
        self.webDriver=WebDriver.getObject(self)
    
    def enterURL(self, url):
        driver=self.webDriver.getDriver()
        driver.get(url)