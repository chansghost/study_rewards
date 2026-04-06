from imports_consts import *

timer_test = 10
DEFAULT_TIME=25
#time buttons are formatted for easy editing, using minutes, and then
#the program converts them into seconds. if changing value, always put it in
#MINUTES
TIME_BUTTON1=25
TIME_BUTTON2=40
TIME_BUTTON3=60

def convert_time(secs):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec

class MainWindow(QMainWindow):
    timer_signal=pyqtSignal(int) #it needs to be outside the constructor,
    #as it would not be recognised as a signal otherwise, but an ordinary variable
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setFixedSize(width, height)

        main_container = QWidget()
        self.setCentralWidget(main_container)
        main_layout = QVBoxLayout(main_container)
        
        self.balanceLabel=QLabel(f'Coins:')
        self.stacked_widget = QStackedWidget()
        
        
        main_layout.addWidget(self.balanceLabel)
        main_layout.addWidget(self.stacked_widget)
        
        
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

    def update_balance(self, balance):
        self.balanceLabel.setText(f'Coins: {balance}')

    def timer_ui(self):
        widget=QWidget()
        layout=QVBoxLayout()
        
        self.duration=DEFAULT_TIME*60
        self.timerLabel = QLabel(f'{self.duration//60}:00')
        
        back_button=QPushButton("Go back")
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        
        preset_btn_layout=QHBoxLayout()
        button_one=QPushButton(f'{TIME_BUTTON1}:00')
        button_two=QPushButton(f'{TIME_BUTTON2}:00')
        button_three=QPushButton(f'{TIME_BUTTON3}:00')
        preset_btn_layout.addWidget(button_one)
        preset_btn_layout.addWidget(button_two)
        preset_btn_layout.addWidget(button_three)
        button_one.clicked.connect(lambda: self.update_timer(TIME_BUTTON1))
        button_two.clicked.connect(lambda: self.update_timer(TIME_BUTTON2))
        button_three.clicked.connect(lambda: self.update_timer(TIME_BUTTON3))

        start_button=QPushButton("Start Timer!")
        restart_button=QPushButton("Restart Timer")
        restart_button.clicked.connect(self.restart_timer)
        
        start_button.clicked.connect(lambda: self.start_timer(self.duration))
        

        layout.addWidget(back_button)
        layout.addWidget(start_button)
        layout.addLayout(preset_btn_layout)
        layout.addWidget(self.timerLabel)
        layout.addWidget(restart_button)
        
        widget.setLayout(layout)
        return widget


    def restart_timer(self):
        if hasattr(self, 'myTimer') and self.myTimer.isActive(): #if the timer even exists and is active
            self.myTimer.stop()
            minsec=convert_time(self.duration)
            self.timerLabel.setText(str(minsec))

    def start_timer(self, duration):
        self.time_left = duration
        self.myTimer = QTimer(self)
        self.myTimer.timeout.connect(lambda: self.timerTimeout(duration))
        self.myTimer.start(1000)
    
    def timerTimeout(self,duration):
        self.time_left-=1
        self.update_timer()

        if self.time_left<=0:
            self.time_left=duration
            self.myTimer.stop()
            self.timer_signal.emit(self.duration)#sending signal about a finished pomodoro
        

    def update_timer(self, new=0):
        if new!=0:
            self.restart_timer()
            self.duration=new*60 #for setting a different timer
            self.time_left=new*60
        minsec=convert_time(self.time_left)
        self.timerLabel.setText(str(minsec))

    


if __name__ in "__main__":
    app=QApplication([])
    system = System()
    user = User("Juls")
    window = MainWindow()

    app_controller = AppController(system, user,window)

    window.show()

    app.exec()
