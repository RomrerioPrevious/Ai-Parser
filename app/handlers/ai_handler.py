import logging
import re
import time

from ..config import CONFIG
from openai import OpenAI, RateLimitError
import httpx


class AiHandler:
    def __init__(self):
        self.delay = CONFIG.ai.min_delay
        if CONFIG.app.proxy:
            self.http_client = httpx.Client(proxy=CONFIG.app.proxy)
            self.ai = OpenAI(
                api_key=CONFIG.ai.api_key,
                base_url="https://api.deepseek.com/v1",
                http_client=self.http_client
            )
        else:
            self.ai = OpenAI(
                api_key=CONFIG.ai.api_key,
                base_url="https://api.deepseek.com/v1"
            )
        with open("resources/prompt.txt", "r", encoding="utf-8") as file:
            self.prompt = file.read()

    def get_price(self, data: str) -> float | str:
        for i in range(5):
            try:
                price_str = self.ask(data)
                price = float(re.findall(r"\d+\.\d+", price_str)[0])
                if price:
                    continue
                return price
            except RateLimitError as e:
                logging.error(e)
                if e.code == "insufficient_quota":
                    raise e
                time.sleep(self.delay)
                self.delay = min(self.delay * 2, CONFIG.ai.max_delay) * (1 + 0.1 * (i % 3))
            except ValueError as e:
                logging.error(f"Error parsing price: {e}")
            except BaseException as e:
                logging.error(e)
        return 0.0

    def ask(self, product: str) -> str:
        response = self.ai.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": f"Find the price of the product: {product}"}
            ],
            temperature=1.8
        )

        price_str = response.choices[0].message.content
        return price_str
