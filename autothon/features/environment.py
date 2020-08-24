from com.source.driver.DriverInit import WebDriver
from behave import fixture
import os   
def before_tag(context, tag):
    print("I am in before tag")
    webDriver=WebDriver()
    
    
def after_tag(context, tag):
    print("I am in after tag")
    webDriver=WebDriver().getObject(WebDriver)
    webDriver.getDriver().quit()
    WebDriver().setObjectToNone()
    deleteFileWithContent("skipped")

def deleteFileWithContent(content):    
    entries = os.listdir('output/allure-reports/')
    for entry in entries:
        print(entry)
        file1 = open('output/allure-reports/' + entry, 'r')
        if content in file1.read():
            os.remove('output/allure-reports/' + entry)


    