from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QDateEdit

class PersonalPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('First Name:', QLineEdit(self))
        layout.addRow('Last Name:', QLineEdit(self))
        layout.addRow('DOB:', QDateEdit(self))
