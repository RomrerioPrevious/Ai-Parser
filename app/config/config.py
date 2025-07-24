from dynaconf import Dynaconf
import logging

CONFIG = Dynaconf(
    settings_files=["resources\config.toml"],
)

logging.basicConfig(
    level=logging.INFO, filename="resources/logs.log", filemode="a",
    datefmt='%Y-%m-%d %H:%M:%S',
    format="%(asctime)s %(levelname)s | %(message)s"
)
