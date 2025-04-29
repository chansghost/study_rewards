from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton, QLabel, QWidget, QGridLayout,QVBoxLayout
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QPixmap

height=820
width=390
path="study_store/"



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(width,height))
        self.setStyleSheet("QWidget { background-image: url('study_store/background.png'); background-repeat: no-repeat; background-position: center; }")
        
        self.study_store()


    def study_store(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(25,50,25,50)
        layout.setSpacing(150)
        #self.label = QLabel("<h1>study store</h1>",alignment=Qt.AlignmentFlag.AlignHCenter)
        self.header=QLabel()
        self.image=QPixmap(path+"studystore.png")#later, instead of an image, there will be text to improve quality
        self.header.setPixmap(self.image)
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.header)
        window = QWidget()
        window.setLayout(layout)
        
        self.setCentralWidget(window)


app=QApplication([])

window = MainWindow()

window.show()

app.exec()
