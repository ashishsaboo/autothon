from selenium import webdriver

class WebDriver:
    __instance = None
    #driver = ""
    
    @staticmethod
    def getObject(self):
        if WebDriver.__instance == None:
            print("Initializing new Driver")
            WebDriver.getChromeDriver(self)
            WebDriver()
        else:
            return WebDriver.__instance
    
    def __init__(self):
        if WebDriver.__instance != None:
            print("")
        else:
            print("this is creating object")
            print("object name:", self)
            WebDriver.getChromeDriver(self)
            WebDriver.__instance=self
            
        
    def getChromeDriver(self):
        if WebDriver.__instance == None:
            print("creating new driver")
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')
            self.driver = webdriver.Chrome(executable_path='resources/drivers/chromedriver', chrome_options=options)
            self.driver.maximize_window()
        else:
            print("using existing driver")
            return self.driver
    
    def getDriver(self):
        return self.driver