from com.source.PageObjects.AutothonRetailLoginPage import AutothonRetailLoginPage


class AutothonRetailLoginTest:
    def __init__(self):
        print("I am in login test")
        self.autothonRetailLoginPage = AutothonRetailLoginPage()
    
    def enterURL(self, url):
        self.autothonRetailLoginPage.enterURL(url)

    def goToLoginPage(self):
        self.autothonRetailLoginPage.goToLoginPage()
        
    def clickSIgnIn(self, userName, password):
        self.autothonRetailLoginPage.signIn(userName, password)
        
    def clickOnSection(self, category, item):
        self.autothonRetailLoginPage.click_On_Section(category, item)
        
    def viewAndCheckoutCart(self):
        self.autothonRetailLoginPage.view_and_checkout_cart()
        
    def clickContinueShopping(self):
        self.autothonRetailLoginPage.clickContinueShopping()
        
    def incrementCartByQty(self, itemName, noOfItem, total):
        return self.autothonRetailLoginPage.increment_product_by_count(itemName, noOfItem, total)
        
    def viewCart(self):
        self.autothonRetailLoginPage.view_cart()
    
    def checkoutCart(self):
        self.autothonRetailLoginPage.checkout_cart()
        
    def verifyOrderDetail(self, userName, total):
        self.autothonRetailLoginPage.checkOrderDetail(userName, total)