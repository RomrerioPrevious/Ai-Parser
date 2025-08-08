import logging
import os
from typing import Any, Generator, Tuple

import pandas as pd
from openai import RateLimitError

from ..config import CONFIG
from .ai_handler import AiHandler
from ..models import Item


class FileHandler:
    def __init__(self, file: str = None, columns: [str] = None):
        self.ai_handler = AiHandler()
        self.columns = columns
        self.max_items = 0
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

    def get_log_dict(self) -> list[str]:
        return self.text

    def parse(self) -> Generator[Tuple[str, bool], Any, None]:
        items = self.get_items_from_file()
        self.max_items = len(items)

        for index, item in enumerate(items):
            try:
                item.price = self.find_price(item)
                self.save_items_to_file(items)
                log = self.make_log(item)
                yield self.generate_text(log), False
            except RateLimitError as e:
                yield self.generate_empty_massage(e.message), False
        yield "Success", True

    def make_log(self, item: Item) -> str:
        if not item.price:
            text = f"No price found for product {item.name}"
            self.counter["error"] += 1
            logging.warning(text)
        else:
            text = f"Product price {item.name} - {item.price}руб"
            self.counter["success"] += 1
            logging.info(text)
        return text


    def generate_text(self, new_text: str) -> str:
        for i in range(23, 2, -1):
            self.text[i] = self.text[i - 1]
        if len(new_text) > 75:
            self.text[2] = "  " + new_text[:72] + "..."
        else:
            self.text[2] = "  " + new_text
        self.text[1] = "--------------------------" * 3
        success = self.counter["success"]
        error = self.counter["error"]
        self.text[0] = f"  Completed: {success + error} / {str(self.max_items)}     Success: {success}     Error: {error}"
        return "\n".join(self.text)

    def generate_empty_massage(self, new_text: str) -> str:
        self.text = [""] * 24
        self.text[2] = "  " + new_text
        self.text[1] = "--------------------------" * 3
        success = self.counter["success"]
        error = self.counter["error"]
        self.text[0] = f"  Completed: {success + error} / {str(self.max_items)}     Success: {success}     Error: {error}"
        return "\n".join(self.text)

    def get_items_from_file(self) -> list[Item]:
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
        return self.ai_handler.get_price(item.name)


    def save_items_to_file(self, items: list[Item]):
        df = pd.DataFrame([vars(item) for item in items])
        df.columns = self.columns
        base, ext = os.path.splitext(self.file)
        df.to_excel(f"{base} (price){ext}", index=False, engine="openpyxl")
