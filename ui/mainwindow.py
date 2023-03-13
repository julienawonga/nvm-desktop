from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget, QPushButton
from PyQt6.QtCore import Qt
from ui.infopage import InfoPage
from ui.actionspage import ActionsPage


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Nvm Desktop')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        self.resize(600, 300)

        # create a tab widget
        tab = QTabWidget(self, movable=True)

        # informations page
        info_page = InfoPage(self)
        tab.addTab(info_page, 'Info')

        # actions page
        actions_page = ActionsPage(self)
        tab.addTab(actions_page, 'Actions')


        main_layout.addWidget(tab, 0, 0, 2, 1)


        self.show()
