from imports_consts import *
from rect import RectangleWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(width,height))
        self.setStyleSheet("QMainWindow { background-image: url('study_store/background.png'); background-repeat: no-repeat; background-position: center; }")
        
        self.study_store()


    def study_store(self):
        layout = QGridLayout()
        layout.setContentsMargins(25,50,25,50)
        layout.setSpacing(150)
        #self.label = QLabel("<h1>study store</h1>",alignment=Qt.AlignmentFlag.AlignHCenter)
        self.header=QLabel()
        self.image=QPixmap(path+"rewards.png")#later, instead of an image, there will be text to improve quality
        self.header.setPixmap(self.image)
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label=QLabel("study store")
        self.label.setFixedHeight(50)
        self.label.setStyleSheet("color: #494949; font-size: 52px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        #self.label.setFont(QFont(fonts[0],80))
        layout.addWidget(self.label)
      #  painter.drawRect(50,50,50,50)
        self.canvas = RectangleWidget()
        layout.addWidget(self.canvas)
        #layout.addWidget(self.header)
        window = QWidget()
        window.setLayout(layout)
        self.canvas.draw_rectangle(50, 50, 100, 60)
        self.setCentralWidget(window)


app=QApplication([])
font_id = QFontDatabase.addApplicationFont("Judson/Judson-Regular.ttf")
if font_id != -1:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    app.setFont(QFont(font_family))
else:
    print("Nie udało się załadować czcionki Judson.")

window = MainWindow()

window.show()

app.exec()
