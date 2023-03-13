# Import the required PyQt6 modules
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QComboBox, QPushButton

# Define a new QWidget subclass called ActionsPage
class ActionsPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a QGridLayout to organize the widgets
        layout = QGridLayout()
        self.setLayout(layout)

        # Create three QPushButton widgets with the labels 'Install', 'Remove', and 'Use'
        add_node_btn = QPushButton('Install')
        remove_node_btn = QPushButton('Remove')
        current_node_btn = QPushButton('Use')

        # Create three QComboBox widgets to allow the user to select different versions
        add_node_combo = QComboBox()
        add_node_combo.addItem('17')  # add an item with the label '17' to the combo box
        add_node_combo.addItem('16')  # add an item with the label '16' to the combo box

        remove_node_combo = QComboBox()
        remove_node_combo.addItem('17')
        remove_node_combo.addItem('16')

        current_node_combo = QComboBox()
        current_node_combo.addItem('17')
        current_node_combo.addItem('16')

        # Add QLabel widgets to provide descriptive text for each QComboBox and QPushButton widget
        layout.addWidget(QLabel('Select Current :'), 0, 0)
        layout.addWidget(current_node_combo, 0, 1)
        layout.addWidget(current_node_btn, 0, 2)

        layout.addWidget(QLabel('Install Version :'),1, 0)
        layout.addWidget(add_node_combo,1, 1)
        layout.addWidget(add_node_btn,1, 2)

        layout.addWidget(QLabel('Remove : '),2, 0)
        layout.addWidget(remove_node_combo,2, 1)
        layout.addWidget(remove_node_btn,2, 2)
