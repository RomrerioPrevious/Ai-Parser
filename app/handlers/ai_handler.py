from ..config import CONFIG
from openai import OpenAI
import httpx


class AiHandler:
    def __init__(self):
        if CONFIG.app.proxy:
            self.http_client = httpx.Client(proxy=CONFIG.app.proxy)
            self.ai = OpenAI(api_key=CONFIG.ai.api_key, http_client=self.http_client)
        else:
            self.ai = OpenAI(api_key=CONFIG.ai.api_key)
        with open("resources/prompt.txt", "r", encoding="utf-8") as file:
            self.prompt = file.read()
        

    def get_price(self, data: str) -> float:
        response = self.ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": f"Find the price of the product: {data}"}
            ],
            temperature=0.0
        )

        price_str = response.choices[0].message.content
        try:
            return float(price_str)
        except ValueError:
            raise ValueError(f"Could not convert AI response to float: {price_str}")
