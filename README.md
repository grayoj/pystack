# pystack.

[Pystack](https://pypi.org/project/pystack-sdk/) is a Python API wrapper designed to streamline Paystack integrations within Python projects, (Django, Flask, etc) Paystack does not natively provide an sdk or wrapper client for Python. I was working on a project once and I found myself writing boilerplate code rather than focusing on integrating payments into my service.

## Features

- Initiate and verify payments with Paystack.
- Resolve card BIN to get card details.
- Resolve account number to get account details.
- Simplify recurring charges and subscriptions with Paystack.

## Getting Started

[The package is available on PyPi](https://pypi.org/project/pystack-sdk/). In any project, run: `pip3 install pystack.`

## Usage

- The first thing to do is to install the `PystackClient.`

```python
from pystack import PystackClient
```

- Obtain your key from Paystack. You could get your key by following these instructions: [Paystack Docs](https://paystack.com/)
- Using the pystack client, create an object with your key.

```python
# Create a PaystackClient object
paystack_client = PystackClient(pystack_key=YOUR_KEY)
```

- You're set to go.

## Making Payments

Below is an example of how the pystack module helps you skip the shenanigans and focus on the payments.

```python

from pystack import PystackClient

# Replace 'YOUR_KEY' with your actual Paystack secret key.
YOUR_KEY = 'YOUR_KEY'

# Create a PaystackClient object
pystack = PystackClient(pystack_key=YOUR_KEY)

# Now we initiate a payment
amount = 5000  # The amount to send in the request
email = 'pystack@pystack.com'  # The customer's email address
payment_response = pystack.initiatePayment(amount=amount, email=email)
```

Look how much boilerplate code you saved above.

## Verifying Transactions

You can also verify transactions through though the pystack module. Here is an example:

```python
from pystack import PystackClient

# Replace 'YOUR_KEY' with your actual Paystack secret key.
YOUR_KEY = 'YOUR_KEY'

# Create a PaystackClient object
pystack = PystackClient(pystack=YOUR_KEY)

# Now we initiate a payment
amount = 5000  # The amount to send in the request
email = 'pystack@pystack.com'  # The customer's email address
payment_response = pystack.initiatePayment(amount=amount, email=email)

# Condition to verify the payment
if payment_response['status']:
    transaction_reference = payment_response['data']['reference']
    verification_response = pystack.verifyPayment(reference=transaction_reference)

    if verification_response['status']:
        print("Payment was successful.")
    else:
        print("Payment verification failed.")
else:
    print("Payment initiation failed.")
```

Like wise there are other things you could do with Pystack, such as recurring charges, subscriptions, etc. It's up to you to decide what you want to do, and then use it.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
