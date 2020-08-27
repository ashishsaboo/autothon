from com.source.driver.DriverInit import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random as rd
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from com.source.PageObjects.ExceptionExample import AutomationError


class AutothonRetailLoginPage:

    def __init__(self):
        print("I am in login page")
        # self.webDriver=WebDriver.getObject(self)

    def enterURL(self, url):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        print("driver in second scenario", driver)
        driver.get(url)

    def goToLoginPage(self):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        #         action = ActionChains(driver)
        #         action.move_to_element(driver.find_element_by_id("dropdownCurrency")).click()
        time.sleep(4)
        driver.find_element_by_link_text("FREE 30 Day Trial").click()
        time.sleep(4)
        driver.find_element_by_id("Form_submitForm_subdomain").send_keys("myemail")
        time.sleep(4)
        num = 1 / 0

    def click_On_Section(self, category, item):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        print(category + item)
        print(category + item)
        print(category + item)
        time.sleep(2)
        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.presence_of_element_located(
            (By.PARTIAL_LINK_TEXT, "Autothon Retail Demo Store - You Select We Deliver!!")))
        print(category + item)
        print(category + item)
        driver.find_element_by_partial_link_text("Autothon Retail Demo Store - You Select We Deliver!!").click()

        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, category)))
        driver.find_element_by_link_text(category).click()
        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='row']/div")))

        wait = WebDriverWait(driver, 20)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='row']/div/div/div/div/a[contains(@href, '#/product/49')]")))
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='" + item + "']")))
        time.sleep(2)
        print(category + item)
        print(category + item)
        print(driver.find_element_by_xpath("//img[@alt='" + item + "']").get_attribute("src"))
        driver.find_element_by_xpath("//img[@alt='" + item + "']").click()
        time.sleep(2)
        wait = WebDriverWait(driver, 20)
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add to Cart')]")))
        driver.find_element_by_xpath("//button[contains(text(),'Add to Cart')]").click()
        print("add to cart clicked")
        time.sleep(2)

    def clickContinueShopping(self):
        time.sleep(2)
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        driver.find_element_by_xpath("//button[contains(text(),'Continue Shopping')]").click()
        time.sleep(2)

    def view_cart(self):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        time.sleep(2)
        wait = WebDriverWait(driver, 20)
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'View Cart')]")))
        driver.find_element_by_xpath("//button[contains(text(),'View Cart')]").click()
        print("View cart clicked")

    def checkout_cart(self):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        time.sleep(2)

        wait = WebDriverWait(driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'Checkout')]")))
        driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
        time.sleep(2)
        self.enter_billing_detail()

    #     def view_and_checkout_cart(self, itemName, noOfItem):
    #         webDriver=WebDriver.getObject(self)
    #         #webDriver=WebDriver()
    #         driver=webDriver.getDriver()
    #         time.sleep(2)
    #         wait=WebDriverWait(driver, 20)
    #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'View Cart')]")))
    #         driver.find_element_by_xpath("//button[contains(text(),'View Cart')]").click()
    #         print("View cart clicked")
    #
    #         self.increment_product_by_count(itemName, noOfItem)
    #
    #         time.sleep(20)
    #         wait=WebDriverWait(driver, 20)
    #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'Checkout')]")))
    #         driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
    #         time.sleep(2)
    #         self.enter_billing_detail()

    def increment_product_by_count(self, itemName, noOfItem, total):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()
        noOfItem = int(noOfItem)
        elem = driver.find_element_by_xpath("//img[@alt='" + itemName + "']/../../td[3]/i")
        itemPrice = driver.find_element_by_xpath("//img[@alt='" + itemName + "']/../../td[4]").text
        itemPrice = itemPrice.replace("$", "").replace(" ", "")
        grandTotal = float(total) + float(itemPrice)
        while noOfItem > 1:
            elem.click()
            noOfItem = noOfItem - 1
            grandTotal = grandTotal + float(itemPrice)

        print("total price:" + str(grandTotal))
        print("total price:" + str(grandTotal))
        return grandTotal

    def enter_billing_detail(self):
        webDriver = WebDriver.getObject(self)
        # webDriver=WebDriver()
        driver = webDriver.getDriver()

        driver.find_element_by_id("firstName").send_keys("autothon")
        driver.find_element_by_id("lastName").send_keys("autothon")
        driver.find_element_by_id("email").send_keys("autothon@gmail.com")

        driver.find_element_by_id("address").send_keys("autothon")
        driver.find_element_by_id("address2").send_keys("autothon")

        country = driver.find_element_by_id("country")
        countryList = Select(country)
        countryList.select_by_visible_text("India")

        state = driver.find_element_by_id("state")
        stateList = Select(state)
        stateList.select_by_visible_text("Karnataka")

        driver.find_element_by_id("zip").send_keys("560066")

        time.sleep(1)
        driver.find_element_by_xpath("//label[@for='same-address']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//label[@for='save-info']").click()
        time.sleep(1)
        driver.find_element_by_id("cc-name").send_keys("autothon")
        driver.find_element_by_id("cc-number").send_keys("11111111111")
        driver.find_element_by_id("cc-expiration").send_keys("01/2025")
        driver.find_element_by_id("cc-cvv").send_keys("2345")
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(text(),'Confirm Order')]").click()

        #         wait=WebDriverWait(driver, 20)
        #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Order Submitted']")))
        #
        #         driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
        time.sleep(2)
        print("user field: " + driver.find_element_by_id("firstName").get_attribute("value"))
        if driver.find_element_by_id("firstName").get_attribute("value") == "":
            print("Order submitted successfully")
        else:
            raise AutomationError("Order Not submitted successfully")

        # time.sleep(2)

    def signIn(self, userName, Password):
        webDriver = WebDriver.getObject(self)
        driver = webDriver.getDriver()
        print("driver in second scenario", driver)
        print("clicking on sign in button")
        driver.find_element_by_link_text("Sign In").click()
        print("clicked on sign in button")
        driver.find_element_by_xpath("//input[@placeholder='Enter your Username']").send_keys(userName)
        driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys(Password)
        driver.find_element_by_xpath("//button[text()='Sign In']").click()
        wait = WebDriverWait(driver, 20)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, userName)))
            print("user logged in successfully")
        except:
            print("user not logged in successfully")
            assert False, "user not logged in successfully"
        userName = driver.find_element_by_partial_link_text(userName)
        print(userName.text);

    #         try :
    #             userName = driver.find_element_by_partial_link_text("Autothonteam3")
    #         except(NoSuchElementException):

    def checkOrderDetail(self, userName, total):
        webDriver = WebDriver.getObject(self)
        driver = webDriver.getDriver()
        time.sleep(2)
        driver.find_element_by_partial_link_text(userName).click()
        time.sleep(2)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(2)
        elemOrderTable = driver.find_elements_by_xpath("//div/table[@class='table']/tr")
        count = 0
        for row in elemOrderTable:
            count = count + 1
        print("number of rows:" + str(count))
        print("number of rows:" + str(count))

        orderId = driver.find_element_by_xpath("//div/table[@class='table']/tr[" + str(count) + "]/td[1]").text
        strUserName = driver.find_element_by_xpath("//div/table[@class='table']/tr[" + str(count) + "]/td[2]").text
        strItem = driver.find_element_by_xpath("//div/table[@class='table']/tr[" + str(count) + "]/td[3]/div").text
        strTotal = driver.find_element_by_xpath("//div/table[@class='table']/tr[" + str(count) + "]/td[4]").text
        print(orderId + strUserName + strItem + strTotal)
        print(orderId + strUserName + strItem + strTotal)
        if str(total) in strTotal:
            print("total order amount matched")
        else:
            print("total order amount not matched: Expected: " + str(total) + " Actual: " + strTotal)
            errStatement = "total order amount not matched: Expected: " + str(total) + " Actual: " + strTotal
            raise AutomationError(errStatement)

    def createAccount(self, username, password, email, countrycode, mobile, result):
        webDriver = WebDriver.getObject(self)
        driver = webDriver.getDriver()
        time.sleep(5)
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_link_text("Create account").click()
        numToAppendForUserName = rd.SystemRandom().randint(100000, 999999)
        if username == "":
            username = username
        else:
            username = username + str(numToAppendForUserName)
        driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(username)
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
        driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(email)
        countryCode = driver.find_element_by_xpath("//select[@data-test='dial-code-select']")
        countryCodeList = Select(countryCode)
        time.sleep(3)
        countryCodeList.select_by_visible_text(countrycode)
        driver.find_element_by_xpath("//input[@placeholder='Phone Number']").send_keys(mobile)
        driver.find_element_by_xpath("//button[text()='Create Account']").click()
        # wait = WebDriverWait(driver, 20)
        if result == "":
            actualResult = driver.find_element_by_xpath("//button[text()='Confirm']").text
            result = 'CONFIRM'
        else:
            actualResult = driver.find_element_by_xpath("//div[2]/div/div[4]").text
        assert result == actualResult, "Test Case Failed due to Actual result :=" + actualResult + "Expected result :=" + result
