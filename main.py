from app import *
from PyQt5.QtWidgets import *
from icecream import ic
import sys

from app.handlers.ai_handler import AiHandler


def main():
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())

    # ai = AiHandler()
    # ai.get_price("Полусфера Bosu Ball Atemi, 58 см, ABS01")
    # print(ai)

if __name__ == "__main__":
    ic.enable()
    logging.info("Program has been started")
    main()
