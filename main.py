from imports_consts import *
from rect import RectangleWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("apka")
        self.setFixedSize(QSize(width,height))
        #self.setStyleSheet("QMainWindow { background-image: url('study_store/background.png'); background-repeat: no-repeat; background-position: center; }")
        self.balance = 127
        self.study_store()
        #self.testing()


    def study_store(self):
        master_layout = QGridLayout()
        master_layout.setContentsMargins(25,50,25,10)
        master_layout.setHorizontalSpacing(2)

        master_layout.setRowStretch(1, -15)
       # master_layout.setRowStretch(2, 1)  


        self.label=QLabel("study store") #does it really need to be a class attribute? to think about later
        self.label.setFixedHeight(60)
        self.label.setObjectName("study_store")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.label.setFont(QFont(fonts[0],80))
        master_layout.addWidget(self.label, 0, 0, 1, -1, Qt.AlignmentFlag.AlignTop)
        # 0, 0 -> 1 wiersz i kolumna gridlayout
        # 1, -1 -> 1 wiersz wysokosci, a -1 sprawia ze ignorujemy kolumny tak jakby i rozciagamy na wws
       # layout.addWidget(self.header)
        self.coins_img = QLabel()
        coins_map = QPixmap(path+'coins.png')
        #coins_image.scaled(42, 42, aspectRatioMode=Qt.IgnoreAspectRatio, mode=Qt.FastTransformation)
        scaled_coins = coins_map.scaled(42, 42, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.coins_img.setPixmap(scaled_coins)
        self.coins_img.setObjectName("coins_img")
        
        self.coins = QLabel("coins")
        self.coins.setObjectName("coins")

        self.coins_bg = QLabel(str(self.balance))
        self.coins_bg.setFixedHeight(52)
        #coins_bg.setFixedSize(QSize(135,50))
        self.coins_bg.setObjectName("coins_bg")
        self.coins_bg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        coin_layout = QHBoxLayout()

        coin_layout.addWidget(self.coins_img)
        coin_layout.addWidget(self.coins)
        coin_layout.addWidget(self.coins_bg)

        master_layout.addLayout(coin_layout,1,0)




        window = QWidget()
        window.setLayout(master_layout)
        self.setCentralWidget(window)
    
    def testing(self):
        layout = QGridLayout()
        #master_layout.setContentsMargins(25,50,25,50)
        layout.addWidget(QLabel("mama"), 0, 1)
        layout.addWidget(QLabel("miala"), 0, 2)
        layout.addWidget(QLabel("bialego"), 0, 3)
        layout.addWidget(QLabel("kotka"), 0, 4)
        layout.addWidget(QLabel("ciocia basia"), 1, 0)
        layout.addWidget(QLabel("ciocia kasia"), 2, 0)
        layout.addWidget(QLabel("kolejny test"), 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


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
