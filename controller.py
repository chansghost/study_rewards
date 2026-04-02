from main import MainWindow
from user import User
from system import System



class AppController:
    def __init__(self, system, user, view):
        self.system=system
        self.user = user
        self.view = view
    
    def signal_service(self):
        self.view.timer_signal.connect(lambda duration: 
                                       self.system.pomodoro_service(duration,self.user)
                                       )
        
