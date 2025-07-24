import pandas as pd

from ..config import CONFIG
from .ai_handler import AiHandler
from ..models import Item


class FileHandler:
    def __init__(self, file=None):
        self.ai_handler = AiHandler()
        if not file:
            self.file = CONFIG.app.path_to_file
        else:
            self.file = file

    def get_items_from_file(self) -> [Item]:
        data = pd.read_excel(self.file)

        result = []

        for index, row in data.iterrows():
            article = row.values[0]
            name = row.values[1]

            result.append(
                Item(name=name, article=article, price=0)
            )

        return result
