from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget, QPushButton
from PyQt6.QtCore import Qt
from ui.infopage import InfoPage
from ui.installationpage import InstallationPage
from ui.selectpage import SelectPage

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        self.resize(600, 400)

        # create a tab widget
        tab = QTabWidget(self, movable=True)

        # personal page
        info_page = InfoPage(self)
        tab.addTab(info_page, 'Personal Info')

        # contact page
        installation_page = InstallationPage(self)
        tab.addTab(installation_page, 'Contact Info')

        #selection page
        select_page = SelectPage(self)
        tab.addTab(select_page, 'Contact Info')


        main_layout.addWidget(tab, 0, 0, 2, 1)


        self.show()
