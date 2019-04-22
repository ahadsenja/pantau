import pandas as pd

from constants import REGION_LIST


class Utils:

    @staticmethod
    def get_region_name_by_code(your_code: str):
        for (code, name) in REGION_LIST:
            if your_code == code:
                return name

        return ''
