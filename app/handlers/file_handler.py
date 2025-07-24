import pandas as pd

from ..config import CONFIG
from .ai_handler import AiHandler
from ..models import Item


class FileHandler:
    def __init__(self, file: str = None, columns: [str] = None):
        self.ai_handler = AiHandler()
        self.columns = columns
        if not file:
            self.file = CONFIG.app.path_to_file
        else:
            self.file = file

    def start_parse(self):
        items = self.get_items_from_file()
        for item in items:
            item.price = self.find_price(item)
        self.save_items_to_file(items)

    def get_items_from_file(self) -> [Item]:
        data = pd.read_excel(self.file)
        result = []

        if not self.columns:
            data = pd.read_excel(self.file)
            self.columns = data.columns.tolist()

        for index, row in data.iterrows():
            article = row.values[0]
            name = row.values[1]

            result.append(
                Item(name=name, article=article, price=0)
            )

        return result

    def find_price(self, item: Item) -> float:
        price = self.ai_handler.get_price(item.name)
        if not price:
            ...  # TODO create error
        return price

    def save_items_to_file(self, items: [Item]) -> bool:
        df = pd.DataFrame([vars(item) for item in items])
        df.columns = self.columns
        df.to_excel(self.file, index=False, engine="openpyxl")
