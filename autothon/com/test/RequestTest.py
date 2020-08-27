from time import sleep
from unicodedata import decimal

from com.source.requests.RequestsServices import *


class RequestTest:

    def __init__(self):
        self.requestService = RequestServices()

    def addProductToCartAndCheckout(self, productType, product, quantity, user):
        print("Add ", productType, " product = ", product, " to cart for the user = ", user)

        url = "http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com/products/category/" + productType
        getResponse = self.requestService.getrequest(url)
        assert getResponse.status_code == 200, "products service status code should be 200"

        jsonData = json.loads(getResponse.text)
        productID = None
        productName = None
        productPrice = None
        flag = False
        for val in jsonData:
            # print(val)
            for k, v in val.items():
                if val.get('name') == product:
                    productID = val.get('id')
                    productName = val.get('name')
                    productPrice = val.get('price')
                    flag = True
                    break
            if flag:
                break
        print("\nProduct ID = ", productID, "\nProduct Name = ", productName, "\nProduct Price = ", productPrice, "\n")

        payloadId = "16"

        url = "http://retai-loadb-2u79u3coh4n6-696888272.us-west-2.elb.amazonaws.com/carts/id/" + payloadId
        if quantity == "":
            quantity = 1
        payload = {
            "id": payloadId,
            "username": user,
            "items": [{"product_id": productID, "quantity": int(quantity), "price": productPrice}]
        }

        response = self.requestService.putrequest(url, payload)
        assert response.status_code == 201, "Add to cart service status code should be 201"

        print("Add to Cart response = ", response.text)

        getResponse = self.requestService.getrequest(url)
        assert getResponse.status_code == 200, "Get cart items service status code should be 200"
        productDetails = json.loads(getResponse.text)
        productValues = productDetails.get('items')
        for key, val in productValues[0].items():
            assert productValues[0].get(
                'product_id') == productID, "Product ID of get cart details should match expected"
            break

        total = int(productPrice) * int(quantity)
        tax = total * 5 / 100
        total = total + tax

        print('Total Amount after 5 % tax', total)

        checkout = {
            "id": "60",
            "username": user,
            "items": [
                {
                    "product_id": productID,
                    "quantity": 1,
                    "price": productPrice
                }
            ],
            "total": total,
            "billing_address": {
                "first_name": "FName",
                "last_name": "LName",
                "email": "",
                "address1": "1234",
                "address2": "123",
                "city": "",
                "state": "KA",
                "zipcode": "5666",
                "country": "IN"
            },
            "channel": "WEB",
            "channel_details": {
                "channel_id": 1,
                "channel_geo": "US"
            }
        }

        url = "http://retai-loadb-gzsy2bwngvg9-1548045595.us-west-2.elb.amazonaws.com/orders"
        response = self.requestService.postrequest(url, checkout)
        assert response.status_code == 201, "Post order service status code should be 201"
        print("Order Service Response = ", response.text)

    def checkAllCategories(self, categoryName):
        url = "http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com/products/category/" + categoryName
        getResponse = self.requestService.getrequest(url)
        print("\nCategory = ", categoryName, " response status code ", getResponse.status_code)
        assert getResponse.status_code == 200, "products service status code should be 200"
        print("\nCategory = ", categoryName, " response text  \n", getResponse.text)

    def checkAllProductsResponse(self, categoryName):
        print("Category = ", categoryName)
        url = "http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com/products/category/" + categoryName
        getResponse = self.requestService.getrequest(url)
        assert getResponse.status_code == 200, "Category service status code should be 200"
        jsonData = json.loads(getResponse.text)

        productUrl = "http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com/products/id/"
        for val in jsonData:
            for k, v in val.items():
                getProductResponse = self.requestService.getrequest(productUrl + val.get('id'))
                print("\nProduct = ", val.get('name'), " response status code =", getProductResponse.status_code)
                assert getProductResponse.status_code == 200, "Products service status code should be 200"
                break

    def checkOrdersResponse(self, userName):
        url = "http://retai-loadb-gzsy2bwngvg9-1548045595.us-west-2.elb.amazonaws.com/orders/username/" + userName
        getOrderResponse = self.requestService.getrequest(url)
        print("\nOrders response status code =", getOrderResponse.status_code, "for user = ", userName)
        assert getOrderResponse.status_code == 200, "Orders service status code should be 200"
        print("\nUser = ", userName, " response text  \n", getOrderResponse.text)
