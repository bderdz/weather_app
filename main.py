from PySide6.QtWidgets import QApplication

from MainWidget import MainWidget


def main():
    app = QApplication()

    widget = MainWidget()
    widget.show()

    return app.exec()

if __name__ == '__main__':
    main()