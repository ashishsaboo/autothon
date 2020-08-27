from locust import HttpUser, task, between

#locust -f PerfTestProdCat.py --headless --host http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com -u 1000 -r 100 -t 30s --csv test-auto --only-summary
class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def get_requests(self):
            self.client.get("/products/category/footwear")
            self.client.get("/products/category/housewares")
            self.client.get("/products/category/beauty")
            self.client.get("/products/category/electronics")
    

    @task(2)
    def add_to_cart(self):
        self.client.put("http://retai-loadb-2u79u3coh4n6-696888272.us-west-2.elb.amazonaws.com/carts/id/3", json={"id": "49", "username": "Autothonteam3", "product_id":"49","quantity":1,"price":89.95})
    

        
    @task(3)
    def checkout_cart(self):
        self.client.post("http://retai-loadb-gzsy2bwngvg9-1548045595.us-west-2.elb.amazonaws.com/orders", json={"id":"49","username":"Autothonteam3","items":[{"product_id":"49","quantity":1,"price":9.99}],"total":20.4895,"billing_address":{"first_name":"FName","last_name":"LName","email":"","address1":"1234","address2":"123","city":"","state":"KA","zipcode":"5666","country":"IN"},"channel":"WEB","channel_details":{"channel_id":1,"channel_geo":"US"}})   
         



