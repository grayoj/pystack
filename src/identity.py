import http.client      
import json

"""
Handle Identity Verification, using Paystack's API
"""
class IdentityVerificationClient:
    def __init__(self, pystack_key):
        self.pystack_key = pystack_key
        self.base_url = "api.paystack.co"

    def _send_request(self, method, path, data=None, params=None):
        connection = http.client.HTTPSConnection(self.base_url)
        headers = {
            "Authorization": f"Bearer {self.pystack_key}",
        }

        if data is not None:
            data = json.dumps(data)
        if params is not None:
            params = "?" + "&".join(f"{k}={v}" for k, v in params.items())

        connection.request(method, path + (params or ""), data=data, headers=headers)
        response = connection.getresponse()
        response_data = json.loads(response.read().decode())
        connection.close()

        return response_data

    """
    Resolve account bin
    """
    def resolve_card_bin(self, card_bin):
        return self._send_request("GET", f"/decision/bin/{card_bin}")

    def resolve_account_number(self, account_number, bank_code):
        params = {
            "account_number": account_number,
            "bank_code": bank_code,
        }
        return self._send_request("GET", "/bank/resolve", params=params)

