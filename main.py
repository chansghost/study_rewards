from imports_consts import *
from rect import RectangleWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(width,height))
        #self.setStyleSheet("QMainWindow { background-image: url('study_store/background.png'); background-repeat: no-repeat; background-position: center; }")
        
        self.study_store()


    def study_store(self):
        layout = QGridLayout()
        layout.setContentsMargins(25,50,25,50)
        layout.setSpacing(150)

        # self.header=QLabel()
        
        # self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label=QLabel("study store")
        self.label.setFixedHeight(60)
        self.label.setObjectName("study_store")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.label.setFont(QFont(fonts[0],80))
        layout.addWidget(self.label, 0, 0, 1, -1, Qt.AlignmentFlag.AlignTop)
        # 0, 0 -> 1 wiersz i kolumna gridlayout
        # 1, -1 -> 1 wiersz wysokosci, a -1 sprawia ze ignorujemy kolumny tak jakby i rozciagamy na wws
       # layout.addWidget(self.header)


        window = QWidget()
        window.setLayout(layout)
        self.setCentralWidget(window)


app=QApplication([])
font_id = QFontDatabase.addApplicationFont("Judson/Judson-Regular.ttf")
if font_id != -1:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    app.setFont(QFont(font_family))
else:
    print("Nie udało się załadować czcionki Judson.")

window = MainWindow()
with open("styles.css", "r") as file:
    app.setStyleSheet(file.read())

window.show()

app.exec()
