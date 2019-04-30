import pandas as pd

from utils import Utils


class Parser(object):
    def __init__(self, data: dict, key1: str = '21', key2: str = '22'):
        self._key1 = key1
        self._key2 = key2
        self._data = data

    def parse(self):
        items = self._data['table'].items()

        region_data = []

        for key, value in items:
            obj = dict({})
            obj['code'] = key
            obj['region'] = Utils.get_region_name_by_code(key)
            obj['value1'] = value[self._key1]
            obj['value2'] = value[self._key2]

            region_data.append(obj)

        return {
            'time_server': self._data['ts'],
            'total_nolsatu': float(self._data['chart'][self._key1]),
            'total_noldua': float(self._data['chart'][self._key2]),
            'process_tps': float(self._data['progress']['proses']),
            'total_tps': float(self._data['progress']['total']),
            'votings': region_data
        }

    def parse_to_csv_format(self):
        items = self._data['table'].items()
        res = []

        for key, value in items:
            obj = dict({})
            obj[Utils.get_region_name_by_code(key)] = {
                'code': key,
                'value1': value[self._key1],
                'value2': value[self._key2]
            }
            res.append(obj)

        return res
