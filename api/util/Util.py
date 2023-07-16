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
