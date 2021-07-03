import hashlib
import hmac
import base64
import time
import json
import requests


class ChatbotMessageSender:

    # chatbot api gateway url
    ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/3610/f3d41163765a8e13925eba340802955713339ff705e27621a18ccafafd30c72d'
    # chatbot custom secret key
    secret_key = 'TnBieXZHcnZsSXNRSWl5U1hJUm1YTEJ2cWtKSU56VVk='

    def __init__(self, type):
        if type == 'housekeeping':
            self.ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/3610/f3d41163765a8e13925eba340802955713339ff705e27621a18ccafafd30c72d'
            self.secret_key = 'TnBieXZHcnZsSXNRSWl5U1hJUm1YTEJ2cWtKSU56VVk='
        elif type == 'reservation':
            self.ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/3679/0e04c93fab5ebbb80335674fe068650f536e497d2345a0d58e495a9cf61b222e'
            self.secret_key = 'TEVkR0tVd0plT2ZiV3Joam5NYldpaUpZalNTZVFhcGk='
        elif type == 'concierge_F&B':
            self.ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/3684/a4bcd6e53ec37b7cbf1f7ae218d261cc76fd7dbc7b62c7aedd6bc5932e949693'
            self.secret_key = 'd2ZYdXFBbFpWUWR5ZVBwV3lWUkxsZVFBb2ZQVnNqQlo='

    def req_message_send(self, msg):

        timestamp = self.get_timestamp()
        request_body = {
            'version': 'v2',
            'userId': 'U47b00b58c90f8e47428af8b7bddcda3d1111111',
            'timestamp': timestamp,
            'bubbles': [
                {
                    'type': 'text',
                    'data': {
                        'description': msg
                    }
                }
            ],
            'event': 'send'
        }

        ## Request body
        encode_request_body = json.dumps(request_body).encode('UTF-8')

        ## make signature
        signature = self.make_signature(self.secret_key, encode_request_body)

        ## headers
        custom_headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-CHATBOT_SIGNATURE': signature
        }

        print("## Timestamp : ", timestamp)
        print("## Signature : ", signature)
        print("## headers ", custom_headers)
        print("## Request Body : ", encode_request_body)

        ## POST Request
        response = requests.post(headers=custom_headers, url=self.ep_path, data=encode_request_body)

        return response

    @staticmethod
    def get_timestamp():
        timestamp = int(time.time() * 1000)
        return timestamp

    @staticmethod
    def make_signature(secret_key, request_body):
        secret_key_bytes = bytes(secret_key, 'UTF-8')
        signing_key = base64.b64encode(hmac.new(secret_key_bytes, request_body, digestmod=hashlib.sha256).digest())

        return signing_key