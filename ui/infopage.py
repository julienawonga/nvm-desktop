# Import the required PyQt6 modules
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout

# Define a new QWidget subclass called InfoPage
class InfoPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a QGridLayout to organize the widgets
        layout = QGridLayout()
        self.setLayout(layout)

        # Add QLabel widgets to display information about the node, npm, and nvm versions
        layout.addWidget(QLabel('Node Version : '), 0, 0)
        layout.addWidget(QLabel('18 lts'), 0, 1)

        layout.addWidget(QLabel('Npm Version : '), 1, 0)
        layout.addWidget(QLabel('6'), 1, 1)

        layout.addWidget(QLabel('Nvm Version : '), 2, 0)
        layout.addWidget(QLabel('2'), 2, 1)
