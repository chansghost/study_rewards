from imports_consts import *

height=600
width=600

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setFixedSize(width, height)
        self.stacked_widget = QStackedWidget()

        self.setCentralWidget(self.stacked_widget)
        self.home_page=self.home_ui()
        self.timer_page=self.timer_ui()

        self.stacked_widget.addWidget(self.home_page)#index 0
        self.stacked_widget.addWidget(self.timer_page)

        
        self.show()

    def home_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        timer_button=QPushButton("Timer")
        timer_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(timer_button)
        widget.setLayout(layout)
        return widget


    def timer_ui(self):
        widget=QWidget()
        layout=QVBoxLayout()

        back_button=QPushButton("Go back")
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(back_button)
        widget.setLayout(layout)
        return widget



    


if __name__ in "__main__":
    app=QApplication([])

    window = MainWindow()

    window.show()

    app.exec()
