import sys
from PyQt6 import QtWidgets, uic


def main():
    app = QtWidgets.QApplication(sys.argv)

    # .ui dosyasını yükle
    window = uic.loadUi("ui/loginv2.ui")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()


