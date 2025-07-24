from ..config import CONFIG
import openai


class AiHandler:
    def __init__(self):
        openai.api_key = CONFIG.ai.api_key
        

    def get_price(self, data) -> float:
        ...