from app import *
from PyQt5.QtWidgets import *
from icecream import ic
import sys


def main():
    # app = QApplication(sys.argv)
    # form = QWidget()
    # ui = Ui()
    # ui.setupUi(form)
    # form.show()
    # sys.exit(app.exec_())

    f = FileHandler(file=r"C:\Users\Asus\Downloads\AiParser-test.xlsx")
    f.start_parse()

if __name__ == "__main__":
    ic.enable()
    logging.info("Program has been started")
    main()
