import json
import os
import time

import pandas as pd

from constants import REGION_LIST


class Utils:

    @staticmethod
    def get_region_name_by_code(your_code: str):
        for (code, name) in REGION_LIST:
            if your_code == code:
                return name

        return ''

    @staticmethod
    def save_json_to_file(folder_name: str, text: dict):
        path = os.path.join(os.getcwd(), 'ppwp_file')
        folder_path = os.path.join(path, folder_name)
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        filepath = os.path.join(folder_path, f'ppwp_{time.time()}.json')
        with open(filepath, 'w') as outfile:
            json.dump(text, outfile)
