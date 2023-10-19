'''
This module performs recurring payments or subscriptions.
'''
import http.client
import json


class PaystackRecurringClient:
    def __init__(self, pystack_key):
        self.pystack_key = pystack_key
        self.base_url = "https://api.paystack.co"

    def _send_request(self, method, path, data=None):
        connection = http.client.HTTPSConnection(self.base_url)
        headers = {
            "Authorization": f"Bearer {self.pystack_key}",
            "Content-Type": "application/json",
        }
        if data is not None:
            data = json.dumps(data)

        connection.request(method, path, data=data, headers=headers)
        response = connection.getresponse()
        response_data = json.loads(response.read().decode())
        connection.close()

        return response_data

    def create_subscription(self, customer_email, plan_code):
        data = {
            "customer": customer_email,
            "plan": plan_code,
        }
        response = self._send_request("POST", "/subscription", data)
        return response

    def charge_subscription(self, subscription_code, authorization_code, email):
        data = {
            "authorization_code": authorization_code,
            "email": email,
        }
        response = self._send_request("POST", f"/subscription/{subscription_code}/enable", data)
        return response

    def disable_subscription(self, subscription_code):
        response = self._send_request("POST", f"/subscription/{subscription_code}/disable")
        return response

