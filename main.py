from app import *
from PyQt5.QtWidgets import *
from icecream import ic
import sys


def main():
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ic.enable()
    main()
