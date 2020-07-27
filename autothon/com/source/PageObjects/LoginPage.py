from com.source.driver.DriverInit import WebDriver
import time

class LoginPage():
    
    def __init__(self):
        print("I am in Login Page")
        
    def executeTest(self): 
        webDriver=WebDriver.getObject(self)
        #webDriver=WebDriver()
        driver=webDriver.getDriver()
        driver.get("https://www.google.co.in")
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(3)
#         print(driver.title)
#         driver.quit()