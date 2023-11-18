import http.client
import json

class Request():
    def __init__(self, url: str, method: str, apikey: str, body):
        self.url = url
        self.method = method
        self.apikey = apikey
        self.body = body
    def run(self) -> str:
        connection = http.client.HTTPConnection("developers.cathaypacific.com")
        headers = {"apikey": self.apikey}
        connection.request(self.method.upper(), self.url, headers, body=json.dumps(self.body))
        response = connection.getresponse()
        data = response.read()
        return data.decode("utf-8")