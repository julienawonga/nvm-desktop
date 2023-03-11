from PyQt6.QtWidgets import QGridLayout,QWidget

def infoPage():
	info_page = QWidget()
    layout = QGridLayout()
    info_page.setLayout(layout)
    layout.addWidget(QLabel('Info Page:'), 0, 0)