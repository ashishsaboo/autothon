from com.source.driver.DriverInit import WebDriver
import time

class EntryPage():
    
    def __init__(self):
        print("I am in Entry Page")
        
    def enterText(self): 
        webDriver=WebDriver.getObject(self)
        driver=webDriver.getDriver()
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(3)
        print(driver.title)
        driver.quit()
        