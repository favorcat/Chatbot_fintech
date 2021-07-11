import hashlib
import hmac
import base64
import time
import json
import requests


class ChatbotMessageSender:

    # chatbot api gateway url
    ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/4968/77e3f050e66436c963a670c543621c663212da0fe0fc4c9d35efc31856db1ef4'
    # chatbot custom secret key
    secret_key = 'd0pJd0tYZHRJUXpETUl3YVZseVBEV3pxVWprYmtsbWY='

    def __init__(self, lang):
        if lang == 'ko':
            self.ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/4965/46097fd4489d8a24d99a333c34b055a49304d70bc81635c15887baa075ed2649';
            self.secret_key = 'cnZHc3ZEZFFvRE1LcHNnZVNvdWlRQVFJRFF5WHB0QWI='
        elif lang == 'ja':
            self.ep_path = 'https://f85ad0f761004c0eab772b79c861c861.apigw.ntruss.com/custom/v1/4967/ba8b8d76e0d18d6d1537770aa41f123285e01a7c33712f656bd9d02a476e5b2e'
            self.secret_key = 'Ym9GaWpkbGRJalZ4dkpFUVNETVRvZlVwSVNQUWN3Yno='


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