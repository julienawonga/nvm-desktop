from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QComboBox, QPushButton

class ActionsPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QGridLayout()
        self.setLayout(layout)

        add_node_btn = QPushButton('Install')
        remove_node_btn = QPushButton('Remove')
        current_node_btn = QPushButton('Use')

        add_node_combo = QComboBox()
        add_node_combo.addItem('17')
        add_node_combo.addItem('16')

        remove_node_combo = QComboBox()
        remove_node_combo.addItem('17')
        remove_node_combo.addItem('16')

        current_node_combo = QComboBox()
        current_node_combo.addItem('17')
        current_node_combo.addItem('16')

        layout.addWidget(QLabel('Select Current :'), 0, 0)
        layout.addWidget(current_node_combo, 0, 1)
        layout.addWidget(current_node_btn, 0, 2)

        layout.addWidget(QLabel('Install Version :'),1, 0)
        layout.addWidget(add_node_combo,1, 1)
        layout.addWidget(add_node_btn,1, 2)

        layout.addWidget(QLabel('Remove : '),2, 0)
        layout.addWidget(remove_node_combo,2, 1)
        layout.addWidget(remove_node_btn,2, 2)
