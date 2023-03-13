from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout

class InfoPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Node Version : '), 0, 0)
        layout.addWidget(QLabel('18 lts'), 0, 1)

        layout.addWidget(QLabel('Npm Version : '), 1, 0)
        layout.addWidget(QLabel('6'), 1, 1)

        layout.addWidget(QLabel('Nvm Version : '), 2, 0)
        layout.addWidget(QLabel('2'), 2, 1)
