from com.test.RequestTest import RequestTest
from behave import given

from behave import use_step_matcher

use_step_matcher("re")


@given('Add product \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" to cart for user \"([^\"]*)\" - webservice')
def addCartTest(context, productType, product, productQuantity, user):
    requestTest = RequestTest()
    requestTest.addProductToCartAndCheckout(productType, product, productQuantity, user)


@given('Check category \"([^\"]*)\" response - webservice')
def addCartTest(context, categoryName):
    requestTest = RequestTest()
    requestTest.checkAllCategories(categoryName)


@given('Check category \"([^\"]*)\" products response - webservice')
def addCartTest(context, categoryName):
    requestTest = RequestTest()
    requestTest.checkAllProductsResponse(categoryName)


@given('Check Orders response for user \"([^\"]*)\" - webservice')
def addCartTest(context, userName):
    requestTest = RequestTest()
    requestTest.checkOrdersResponse(userName)
