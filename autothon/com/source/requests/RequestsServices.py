import json

import requests


class RequestServices:
    rootUrl = "http://retai-loadb-1ro1zga66fgow-82429715.us-west-2.elb.amazonaws.com/"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def getrequest(self, url):
        return requests.request("GET", url, headers=self.headers, data=self.payload)

    def putrequest(self, url, payload):
        return requests.request("PUT", url, headers=self.headers, data=json.dumps(payload))

    def postrequest(self, url, payload):
        return requests.post(url, headers=self.headers, data=json.dumps(payload))

    def optionrequest(self, url, payload):
        return requests.options(url, headers=self.headers, data=json.dumps(payload))
