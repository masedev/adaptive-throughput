import requests
import utils.config as config
import json
import time


conf = config.ConfigClass()

class HTTPSimulator:
    def __init__(self, endpoint, method="GET", headers=None, params=None, data=None, json_data=None):
        self.endpoint = endpoint
        self.method = method.upper()
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.json_data = json_data
    
    def send_request(self):
        try:
            response = None
            if self.method == 'GET':
                response = requests.get(self.endpoint, headers=self.headers, params=self.params)
            elif self.method == 'POST':
                response = requests.post(self.endpoint, headers=self.headers, params=self.params, data=self.data, json=self.json_data)
            elif self.method == 'PUT':
                response = requests.put(self.endpoint, headers=self.headers, params=self.params, data=self.data, json=self.json_data)
            elif self.method == 'DELETE':
                response = requests.delete(self.endpoint, headers=self.headers, params=self.params)
            else:
                return f"Unsupported HTTP method: {self.method}"
            

            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": response.text
            }
        
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}




def startup():
    
    with open(conf.payload_folder, 'r') as file:
        data = json.load(file)

    simulator = HTTPSimulator(
        endpoint=conf.endpoint,
        method=conf.method,
        headers={"Content-Type": conf.content_type},
        params=data['parameters']
    )

    while True:
        response = simulator.send_request()
        print(response)
        time.sleep(5)


startup()