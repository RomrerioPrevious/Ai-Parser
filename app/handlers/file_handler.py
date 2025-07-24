import logging
from typing import Any, Generator, Tuple

import pandas as pd
from PyQt5.QtWidgets import QLabel

from ..config import CONFIG
from .ai_handler import AiHandler
from ..models import Item


class FileHandler:
    def __init__(self, file: str = None, columns: [str] = None):
        self.ai_handler = AiHandler()
        self.columns = columns
        self.text = [""] * 24
        self.counter = {
            "success": 0,
            "error": 0
        }
        if not file:
            self.file = CONFIG.app.path_to_file
        else:
            self.file = file

    def get_log(self) -> str:
        return "\n".join(self.text)

    def parse(self, widget: QLabel = None) -> Generator[Tuple[str, bool], Any, None]:
        items = self.get_items_from_file()

        for index, item in enumerate(items):
            item.price = self.find_price(item)
            log = self.log(index, item, items, widget)
            yield self.generate_text(log, index, len(items)), False

        self.save_items_to_file(items)
        yield "Success", True

    def log(self, index, item, items, widget) -> str:
        if not item.price:
            text = f"No price found for product {item.name}"
            self.counter["error"] += 1
            logging.warning(text)
        else:
            text = f"Product price {item.name} {item.price}"
            self.counter["success"] += 1
            logging.info(text)
        return text


    def generate_text(self, new_text: str, index: int, max_items: int) -> str:
        if self.text[21] == "":
            for i in range(22):
                if not self.text[i]:
                    self.text[i] = new_text
                    break
        else:
            for i in range(21):
                self.text[i] = self.text[i + 1]
            self.text[21] = new_text
        self.text[22] = "--------------------------" * 3
        success = self.counter["success"]
        error = self.counter["error"]
        self.text[23] = f"Completed: {success + error} / {str(max_items)}     Success: {success}    Error: {error}"
        return "\n".join(self.text)

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
