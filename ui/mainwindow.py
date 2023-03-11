from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget, QPushButton
from PyQt6.QtCore import Qt
from ui.personalpage import PersonalPage
from ui.contactpage import ContactPage

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self, movable=True)

        # personal page
        personal_page = PersonalPage(self)
        tab.addTab(personal_page, 'Personal Info')

        # contact page
        contact_page = ContactPage(self)
        tab.addTab(contact_page, 'Contact Info')

        main_layout.addWidget(tab, 0, 0, 2, 1)
        main_layout.addWidget(QPushButton('Save'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0,
                              alignment=Qt.AlignmentFlag.AlignRight)

        self.show()
