from time import sleep
from unicodedata import decimal

from com.source.requests.RequestsServices import *


class RequestTest:

    def __init__(self):
        self.requestService = RequestServices()

    def addProductToCartAndCheckout(self, productType, product, user):
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

        payloadId = "115"

        url = "http://retai-loadb-2u79u3coh4n6-696888272.us-west-2.elb.amazonaws.com/carts/id/" + payloadId
        payload = {
            "id": payloadId,
            "username": user,
            "items": [{"product_id": productID, "quantity": 1, "price": productPrice}]
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

        total = float(productPrice) * 5 / 100
        total = total + float(productPrice)

        print('Total after 5 % tax', total)

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
