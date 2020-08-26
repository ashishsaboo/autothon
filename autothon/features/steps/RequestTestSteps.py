from com.test.RequestTest import RequestTest
from behave import given

from behave import use_step_matcher

use_step_matcher("re")


@given('Add product \"([^\"]*)\" \"([^\"]*)\" to cart for user \"([^\"]*)\"')
def addCartTest(context, productType, product, user):
    requestTest = RequestTest()
    requestTest.addProductToCartAndCheckout(productType, product, user)
