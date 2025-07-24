import pandas as pd

from ..config import CONFIG
from .ai_handler import AiHandler
from ..models import Item


class FileHandler:
    def __init__(self):
        self.ai_handler = AiHandler()
        self.input = CONFIG.app.path_to_input_file
        self.output = CONFIG.app.path_to_output_file

    def get_items_from_file(self) -> [Item]:
        with open(self.input, "r") as file:
            data = pd.read_excel(file)

