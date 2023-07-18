import time
from typing import Any
from datetime import datetime

import json


class Util:

    @staticmethod
    def load_json(filepath: str) -> Any:
        with open(file=filepath, mode='r', encoding='UTF-8') as file:
            return json.load(file)

    @staticmethod
    def get_current_semester() -> int:
        current_month = datetime.now().month

        return 1 if 1 <= current_month <= 6 else 2

    @staticmethod
    def compare_times(time_1: str, time_2: str) -> int:
        time_format_1 = '%H:%M:%S'
        time_format_2 = '%H:%M'

        try:
            time_1 = datetime.strptime(time_1, time_format_1).time()
        except ValueError:
            time_1 = datetime.strptime(time_1, time_format_2).time()

        try:
            time_2 = datetime.strptime(time_2, time_format_1).time()
        except ValueError:
            time_2 = datetime.strptime(time_2, time_format_2).time()

        return 0 if time_1 == time_2 else 1 if time_1 > time_2 else -1
