import http.client
import json

class PystackClient:
    def __init__(self, pystack_key):
        self.pystack_key = pystack_key
        self.base_url = "https://api.paystack.co"
    
    def send_request(self, method, path, data=None):
        connection = http.client.HTTPSConnection(self.base_url)
        headers = {
                "Authorization": f"Bearer {self.pystack_key}",
                "Content-Type": "application/json",
                }
        if data is not None;
            data = json.dumps(data)

        connection.request(method, path, data=data, headers=headers)
        response = connection.getresponse()
        response_data = json.loads(response.read().decode())
        connection.close()

    # Initiate Payment. User extends this into their app to intitiate a payment, See the docs. 
    def initiatePayment(self, amount, email):
        data = {
            "amount": amount * 100,  
            "email": email,
        }
        response = self._send_request("POST", "/transaction/initialize", data)
        return response
    
    # Verify payment using reference code.
    def verifyPayment(self, reference):
        response = self._send_request("GET", f"/transaction/verify/{reference}")
        return response
