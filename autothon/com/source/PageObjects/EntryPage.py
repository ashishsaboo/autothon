from com.source.driver.DriverInit import WebDriver
import time

class EntryPage():
    
    def __init__(self):
        print("I am in Entry Page")
        
    def enterText(self, url): 
        print("")
        webDriver=WebDriver.getObject(self)
        print("webdriver == ", webDriver)
        print("webdriver == ", webDriver)
        driver=webDriver.getDriver()
        print("drivers ==", driver)
        print("drivers ==", driver)
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(3)
        print(driver.title)
        