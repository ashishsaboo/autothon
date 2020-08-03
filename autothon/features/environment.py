from com.source.driver.DriverInit import WebDriver
from behave import fixture
   
def before_tag(context, tag):
    print("I am in before tag")
    webDriver=WebDriver()
    
def after_tag(context, tag):
    print("I am in after tag")
    webDriver=WebDriver().getObject(WebDriver)
    webDriver.getDriver().quit()
    