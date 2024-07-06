from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
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

        self.setWindowTitle("Inventory Management System")

        self.setMinimumSize(600, 300)
        self.setMaximumSize(700, 400)


        self.initUI()

    def initUI(self) -> None:
        """
            Load the main components and widgets of the
            user interface
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        title_label = QLabel("Inventory Management System")
        title_label.setAlignment(Qt.AlignHCenter)
        main_layout.addWidget(title_label)

        title_label.setAlignment(Qt.AlignHCenter)

        central_widget.setLayout(main_layout)

        button_layout = QHBoxLayout()

        manage_products_button = QPushButton("Manage products")
        manage_products_button.setFixedWidth(120)
        manage_products_button.setFixedHeight(30)

        generate_reports_button = QPushButton("Generate reports")
        generate_reports_button.setFixedWidth(120)
        generate_reports_button.setFixedHeight(30)

        configure_alerts_button = QPushButton("Configure alerts")
        configure_alerts_button.setFixedWidth(120)
        configure_alerts_button.setFixedHeight(30)

        exit_button = QPushButton("Exit")
        exit_button.setFixedWidth(120)
        exit_button.setFixedHeight(30)

        button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 5px;
                border: 1px solid #2980b9;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 1px solid #1c6ea4;
            }
        """

        manage_products_button.setStyleSheet(button_style)
        generate_reports_button.setStyleSheet(button_style)
        configure_alerts_button.setStyleSheet(button_style)
        exit_button.setStyleSheet(button_style)

        button_layout.addWidget(manage_products_button)
        button_layout.addWidget(generate_reports_button)
        button_layout.addWidget(configure_alerts_button)
        button_layout.addWidget(exit_button)

        main_layout.addLayout(button_layout)


if __name__ == "__main__":
    app = QApplication([])
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())
