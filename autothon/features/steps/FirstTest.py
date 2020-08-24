from com.test.LoginTest import LoginTest
from behave import given
from com.test.EntryTest import EntryTest
from behave import use_step_matcher
from com.test.ListTest import ListTest
use_step_matcher("re")

    
@given('I login with \"([^\"]*)\" and \"([^\"]*)\"')
def i_login_with_user_password(context, username, password):
    print("I am in login Steps", username)
    loginTest = LoginTest()
    loginTest.loginToApplication()
#     entryTest= EntryTest()
#     entryTest.enterToApplication()
    
@given('login with credential')
def login_with_credentials(context):
    print("I am in credentials steps- start")
    lst=[];
    for row in context.table:
        lst.append(row['User'])
        lst.append(row['Password'])
    listTest=ListTest()
    listTest.printListValues(lst)
    entryTest= EntryTest()
    entryTest.enterToApplication("http://gmail.com")
    entryTest.enterToApplication("http://yahoo.com")