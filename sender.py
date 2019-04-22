import requests
import os


class Sender(object):
    def __init__(self, post_url: str):
        self._post_url = post_url

    def send(self, data: dict):
        header = {
            ''
        }
        req = requests.post(self._post_url)
        