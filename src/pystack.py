"""
Pystack Client - Gerald Maduabuchi (2023)
MIT LICENSE
Lightweight client to facilitate authenticating to Paystack's official API.
Kindly see the documentation for better assistance.
"""

import http.client
import json
from .identity_verification import IdentityVerificationClient
from .recurring import PaystackRecurringClient

class PystackClient:

    def __init__(self, pystack_key):
        self.pystack_key = pystack_key
        self.base_url = "https://api.paystack.co"
        self.identity_verification = IdentityVerificationClient(pystack_key)
        self.recurring = PaystackRecurringClient(pystack_key)
    
    def send_request(self, method, path, data=None):
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

    # Perform identity verification.
    def resolve_card_bin(self, card_bin):
        return self.identity_verification.resolve_card_bin(card_bin)

    def resolve_account_number(self, account_number, bank_code):
        return self.identity_verification.resolve_account_number(account_number, bank_code)

    # For recurring charges and subscriptions.
    def create_subscription(self, customer_email, plan_code):
        return self.recurring.create_subscription(customer_email, plan_code)

    def charge_subscription(self, subscription_code, authorization_code, email):
        return self.recurring.charge_subscription(subscription_code, authorization_code, email)

    def disable_subscription(self, subscription_code):
        return self.recurring.disable_subscription(subscription_code)
