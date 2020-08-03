from com.test.PHPTravelLoginTest import PHPTravelLoginTest
from behave import use_step_matcher
use_step_matcher("re")
from behave import given

@given('I get \"([^\"]*)\"')
def step_impl_url(context, url):
    print("I am in get url step", url)
    phpTravelLoginTest = PHPTravelLoginTest()
    phpTravelLoginTest.enterURL(url)
    
@given('I login to Application using \"([^\"]*)\" and \"([^\"]*)\"')
def step_impl_login(context, userName, passowrd):
    print("I am in get url step", userName)
    phpTravelLoginTest = PHPTravelLoginTest()
    phpTravelLoginTest.goToLoginPage()
    
    