from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QSize,Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(300,400))
        self.study_store()
       

    def button_clicked_act(self):
        self.button.setText("nacisnales mnie ala")
        self.label.setText("<h1>to bolalo ty brutalu</h1>")

    def study_store(self):
        layout = QVBoxLayout()
        self.label = QLabel("<h1>study store</h1>",alignment=Qt.AlignmentFlag.AlignHCenter)
        self.button = QPushButton("kliknij")
        self.button.clicked.connect(self.button_clicked_act)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        window = QWidget()
        window.setLayout(layout)
        
        self.setCentralWidget(window)


app=QApplication([])

window = MainWindow()

window.show()

app.exec()
