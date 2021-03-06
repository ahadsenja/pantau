import time

import requests

from utils import Utils


class Crawler(object):
    """
    """

    def __init__(self, target_url: str, verify_ssl: bool = True):
        self._tagret_url = target_url
        self._verify_ssl = verify_ssl

    def set_target_url(self, target_url: str):
        """
        ANother way to set target url
        """
        self._tagret_url = target_url
        return self._tagret_url

    def get_json_data(self):
        """
        get json data from target url
        """
        req = requests.get(self._tagret_url, verify=self._verify_ssl)
        try:
            json = req.json()
            Utils.save_json_to_file(json['ts'], json)

            return json
        except requests.exceptions.RequestException as err:
            print(err)
