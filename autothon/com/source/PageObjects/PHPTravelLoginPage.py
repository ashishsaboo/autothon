from com.source.driver.DriverInit import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class PHPTravelLoginPage:
    def __init__(self):
        print("I am in PHP travel login page")
        #self.webDriver=WebDriver.getObject(self)
    
    def enterURL(self, url):
        webDriver=WebDriver.getObject(self)
        #webDriver=WebDriver()
        driver=webDriver.getDriver()
        print("driver in second scenario", driver)
        driver.get(url)
        
    def goToLoginPage(self):
        webDriver=WebDriver.getObject(self)
        #webDriver=WebDriver()
        driver=webDriver.getDriver()
#         action = ActionChains(driver)
#         action.move_to_element(driver.find_element_by_id("dropdownCurrency")).click()
        time.sleep(4)
        driver.find_element_by_link_text("FREE 30 Day Trial").click()
        time.sleep(4)
        driver.find_element_by_id("Form_submitForm_subdomain").send_keys("myemail")
        time.sleep(4)
        num = 1/0
        