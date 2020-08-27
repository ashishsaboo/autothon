from com.source.driver.DriverInit import WebDriver
from behave import fixture
import os
from allure_commons.types import AttachmentType
import allure


def before_tag(context, tag):
    if tag != "webservice":
        print("I am in before tag")
        webDriver = WebDriver()
        curr_work_dir = os.getcwd()
        print("directory creation for output : " + str(os.path.exists(curr_work_dir + '/output/')))
        if not os.path.exists(curr_work_dir + '/output/'):
            os.makedirs(curr_work_dir + '/output/')
        print("directory creation for log: " + str(curr_work_dir + '/output/log/'))
        if not os.path.exists(curr_work_dir + '/output/log/'):
            os.makedirs(curr_work_dir + '/output/log/')
        print("directory creation for screenshots: " + str(curr_work_dir + '/output/screenshots/'))
        if not os.path.exists(curr_work_dir + '/output/screenshots/'):
            os.makedirs(curr_work_dir + '/output/screenshots/')


def after_tag(context, tag):
    if tag != "webservice":
        print("I am in after tag")
        webDriver = WebDriver().getObject(WebDriver)
        driver = webDriver.getDriver()
        driver.quit()
        WebDriver().setObjectToNone()
        deleteFileWithContent("skipped")


def after_step(context, step):
    if step.name.find("webservice") == -1:
        if step.status == "failed":
            print("I am in after step")
            webDriver = WebDriver().getObject(WebDriver)
            driver = webDriver.getDriver()
            curr_work_dir = os.getcwd()
            # driver.get_screenshot_as_file(curr_work_dir + '/output/screenshots' + "/" + context.scenario.name + ".jpg")
            # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def deleteFileWithContent(content):
    entries = os.listdir('output/allure-reports/')
    for entry in entries:
        # print(entry)
        if "." in entry:
            file1 = open('output/allure-reports/' + entry, 'r')
            if content in file1.read():
                os.remove('output/allure-reports/' + entry)
