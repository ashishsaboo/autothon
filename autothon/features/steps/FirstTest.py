from com.test.LoginTest import LoginTest
from behave import given
from com.test.EntryTest import EntryTest

class FirstTest:
    
    @given("I login")
    def I_Login(self):
        print("I am in login Steps")
        loginTest = LoginTest()
        loginTest.loginToApplication()
        entryTest= EntryTest()
        entryTest.enterToApplication()