from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QWidget,
)
from PySide6.QtCore import Qt
import sys

class DashboardWindow(QMainWindow):
    def __init__(self) -> None:
        """
            Set window size and title
        """
        super().__init__()

        self.setMinimumSize(400, 300)
        self.setMaximumSize(500, 400)

        self.setWindowTitle("Inventory Management System")

        self.initUI()

    def initUI(self) -> None:
        """
            Load the main components and widgets of the
            user interface
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        title_label = QLabel("Inventory Management System")

        title_label.setAlignment(Qt.AlignHCenter)

        main_layout = QGridLayout()
        main_layout.addWidget(title_label)

        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication([])
    window = DashboardWindow()
    window.show()

    with open("style.qss", "r+") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
