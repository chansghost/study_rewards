from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(300,400))
        layout = QVBoxLayout()
        self.label = QLabel("<h1>hejka naklejka</h1>")
        self.button = QPushButton("kliknij")
        self.button.clicked.connect(self.button_clicked_act)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        window = QWidget()
        window.setLayout(layout)
        
        self.setCentralWidget(window)
       

    def button_clicked_act(self):
        self.button.setText("nacisnales mnie ala")
        self.label.setText("<h1>to bolalo ty brutalu</h1>")


app=QApplication([])

window = MainWindow()

window.show()

app.exec()
