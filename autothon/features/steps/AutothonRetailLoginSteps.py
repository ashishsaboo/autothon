from com.test.AutothonRetailLoginTest import AutothonRetailLoginTest
from behave import use_step_matcher
use_step_matcher("re")
from behave import given, then

total = 0
@given('I open \"([^\"]*)\"')
def step_impl_url(context, url):
    print("I am in get url step", url)
    autothonRetailLoginTest = AutothonRetailLoginTest()
    autothonRetailLoginTest.enterURL(url)
    
@given('I login to Application using \"([^\"]*)\" and \"([^\"]*)\"')
def step_impl_login(context, userName, passowrd):
    print("I am in get url step", userName)
#     phpTravelLoginTest = PHPTravelLoginTest()
#     phpTravelLoginTest.goToLoginPage()
    
    
@given('I Login with \"([^\"]*)\" and \"([^\"]*)\"')
def step_impl_signIn(context, userName, password):
    autothonRetailLoginTest = AutothonRetailLoginTest()
    autothonRetailLoginTest.clickSIgnIn(userName, password)
    
@given('I select \"([^\"]*)\" from \"([^\"]*)\"')
def step_impl_section(context, item, category):
    autothonRetailLoginTest = AutothonRetailLoginTest()
    autothonRetailLoginTest.clickOnSection(category, item)
    
@then('I checkout')
def step_impl_checkout(context):
    autothonRetailLoginTest = AutothonRetailLoginTest()
    autothonRetailLoginTest.viewAndCheckoutCart()
    
@given('I select Item from Category and checkout')
def step_impl_select_category_and_item(context):
    lst=[];
    autothonRetailLoginTest = AutothonRetailLoginTest()
    count=1
    for row in context.table:
        count = count +1
    print("value of count:" + str(count))    
    print("value of count:" + str(count)) 
    for row in context.table:
        lst.append(row['Category'])
        lst.append(row['Item'])
        print("value of table:" + row['Category'] + row['Item']) 
        print("value of table:" + row['Category']+ row['Item']) 
        autothonRetailLoginTest.clickOnSection(row['Category'], row['Item'])
        if count > 2 :
            autothonRetailLoginTest.clickContinueShopping()
            count = count -1
    autothonRetailLoginTest.viewCart()
    global total
    for row in context.table:
        total = autothonRetailLoginTest.incrementCartByQty(row['Item'], row['Quantity'], total)
    print("total value from order:: " + str(total))    
    print("total value from order:: " + str(total))
    print("total value from order:: " + str(total))
    tax = round(total * .05, 2)
    print("total value from order:: " + str(tax))
    changeToINR = total * 77
    if changeToINR <10000:
        total = total + 10
    total = total + tax
    autothonRetailLoginTest.checkoutCart()
    
@given('Verify Order detail for \"([^\"]*)\"')
def step_impl_verify_order(context, userName):
    print("total from previous" + str(total))
    print("total from previous" + str(total))
    autothonRetailLoginTest = AutothonRetailLoginTest()
    autothonRetailLoginTest.verifyOrderDetail(userName, total)
        