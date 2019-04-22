import requests
import json


class Sender(object):
    def __init__(self, post_url: str, auth_token: str):
        self._post_url = post_url
        self._auth_token = auth_token

    def send(self, data: dict):
        headers = {
            'Authorization': f'Token {self._auth_token}',
            'Content-Type': 'application/json',
        }
        req = requests.post(self._post_url, data=json.dumps(data), headers=headers)
        return req
