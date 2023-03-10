import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QGridLayout, 
    QTabWidget, 
    QLabel,
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resize(500, 500)
        self.setWindowTitle('NVM DESKTOP')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # info page
        
        # use page
        

        # install page
        
        # remove page
        


        # add pane to the tab widget
        tab.addTab(info_page, 'Personal Info')
        tab.addTab(use_page, 'Remove')
        tab.addTab(install_page, 'Contact Info')
        tab.addTab(remove_page, 'Remove')

        main_layout.addWidget(tab, 0, 0, 2, 1)

        self.show()

    def infoPage(self):
        info_page = QWidget(self)
        layout = QGridLayout()
        info_page.setLayout(layout)
        layout.addWidget(QLabel('Info Page:'), 0, 0)

    def usePage(self):
        use_page = QWidget(self)
        layout = QGridLayout()
        use_page.setLayout(layout)
        layout.addWidget(QLabel('Use Page:'), 0, 0)

    def installPage(self):
        install_page = QWidget(self)
        layout = QGridLayout()
        install_page.setLayout(layout)
        layout.addWidget(QLabel('Installation Page:'), 0, 0)

    def removePage(self):
        remove_page = QWidget(self)
        layout = QGridLayout()
        remove_page.setLayout(layout)
        layout.addWidget(QLabel('Remove Page:'), 0, 0)
        
    def ui():
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())