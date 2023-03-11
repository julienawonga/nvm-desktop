from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit

class ContactPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('Phone Number:', QLineEdit(self))
        layout.addRow('Email Address:', QLineEdit(self))
