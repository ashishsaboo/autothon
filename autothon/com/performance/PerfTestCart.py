from locust import HttpUser, task, between

#locust -f PerfTestProdCat.py --headless --host http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com -u 1000 -r 100 -t 30s --csv test-auto --only-summary
class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def get_requests_for_footwear(self):
        self.client.get("/products/category/footwear")
    
    
#     @task(2)
#     def post_request_for_footwear(self):
#         #self.client.post("/session", {"authenticity_token": "maCu07l39ufNWjhhoYhIvCO04hZnXaSOFRgK1R95HxsYS0W9vXcLs0CS52L/5e2vscR3BKoEJ4EA9XUV737QbA==","login": "ashishsaboo06@gmail.com","password": "phalgun@10", "Content-Type": "application/x-www-form-urlencoded"})
#         
#         self.client.post("http://retai-loadb-2u79u3coh4n6-696888272.us-west-2.elb.amazonaws.com/carts/id/carts/id/13", {"id": "13", "username": "Autothonteam3", "items": [{"product_id": 13, "quantity": 1, "price": "83.5"}]})
#     
#@task(2)
#     def index(self):
#         self.client.get("http://localhost:5000/index")
#         self.client.post("/login", {"username":"admin", "password":"admin"})

