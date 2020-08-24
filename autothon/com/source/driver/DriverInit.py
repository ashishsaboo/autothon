from selenium import webdriver
from jproperties import Properties
import platform

class WebDriver:
    __instance = None
    driver = ""
    
    @staticmethod
    def getObject(self):
        if WebDriver.__instance == None:
            print("Initializing new Driver")
            WebDriver.getChromeDriver(self)
            #WebDriver()
        else:
            return WebDriver.__instance
    
    @staticmethod
    def setObjectToNone():
        WebDriver.__instance=None
        
    def __init__(self):
        if WebDriver.__instance != None:
            print("driver already created", WebDriver.__instance)
        else:
            print("this is creating object")
            print("object name:", self)
            WebDriver.getChromeDriver(self)
            WebDriver.__instance=self
            
        
    def getChromeDriver(self):
        if WebDriver.__instance == None:
            print("creating new driver")
            options = webdriver.ChromeOptions()
            prop = Properties()
            with open('resources/properties/config.properties', 'rb') as config_file:
                prop.load(config_file)
            print(prop.get("ENV"))
            print(platform.system())
            if platform.system() == 'Linux':
                options.add_argument('--no-sandbox')
                options.add_argument('headless')
                options.add_argument('window-size=1200x600')
                options.add_argument('--disable-dev-shm-usage')
                self.driver = webdriver.Chrome(executable_path='resources/drivers/chromedriver-linux', chrome_options=options)
            elif platform.system() == 'Darwin':
                self.driver = webdriver.Chrome(executable_path='resources/drivers/chromedriver-mac', chrome_options=options)
            else:
                self.driver = webdriver.Chrome(executable_path='resources/drivers/chromedriver.exe', chrome_options=options)
            self.driver.maximize_window()
        else:
            print("using existing driver")
            return self.driver
    
    def getDriver(self):
        return self.driver