from com.test.PHPTravelLoginTest import PHPTravelLoginTest
from behave import use_step_matcher
from behave import given
import time
use_step_matcher("re")

@given('I get \"([^\"]*)\"')
def step_impl_url(context, url):
    print("I am in get url step", url)
    phpTravelLoginTest = PHPTravelLoginTest()
    phpTravelLoginTest.enterURL(url)
    
    