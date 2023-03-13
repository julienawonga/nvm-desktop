# Import the required modules
import sys
from PyQt6.QtWidgets import QApplication

# Import the MainWindow class from its module
from ui.mainwindow import MainWindow

# The if statement checks if this script is the main entry point of the program
if __name__ == '__main__':
    # Create a new QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of the MainWindow class
    window = MainWindow()

    # Start the application event loop and wait for it to finish
    sys.exit(app.exec())
