# Import the required PyQt6 modules
from PyQt6.QtWidgets import QWidget, QGridLayout, QTabWidget
from PyQt6.QtCore import Qt

# Import the InfoPage and ActionsPage classes from their respective modules
from ui.infopage import InfoPage
from ui.actionspage import ActionsPage

# Define a new QWidget subclass called MainWindow
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the window title
        self.setWindowTitle('Nvm Desktop')

        # Create a QGridLayout to organize the widgets in the window
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # Set the initial size of the window
        self.resize(600, 300)

        # Create a QTabWidget to hold the InfoPage and ActionsPage widgets
        tab = QTabWidget(self, movable=True)

        # Create an instance of the InfoPage and add it to the QTabWidget
        info_page = InfoPage(self)
        tab.addTab(info_page, 'Info')

        # Create an instance of the ActionsPage and add it to the QTabWidget
        actions_page = ActionsPage(self)
        tab.addTab(actions_page, 'Actions')

        # Add the QTabWidget to the main layout of the window
        main_layout.addWidget(tab, 0, 0, 2, 1)

        # Show the window
        self.show()
