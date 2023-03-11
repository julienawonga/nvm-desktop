from PyQt6.QtWidgets import QTabWidget, QGridLayout, QWidget, QLabel
from PyQt6.QtCore import Qt

from gui.widgets.info_page import infoPage

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resize(500, 500)
        self.setWindowTitle('NVM DESKTOP')

        main_layout = QGridLayout(self)

        #QLayout(main_layout)
        self.setLayout(main_layout)

        #create a tab widget
        tab = QTabWidget(self)

        # add pane to the tab widget
        tab.addTab(infoPage(), 'Personal Info')
        tab.addTab(use_page, 'Remove')
        tab.addTab(install_page, 'Contact Info')
        tab.addTab(remove_page, 'Remove')

        main_layout.addWidget(tab, 0, 0, 2, 1)

        self.show()

        
    def ui():
        ...
