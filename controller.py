#from main import MainWindow
from user import User
from system import System



class AppController:
    def __init__(self, system, user, view):
        self.system=system
        self.user = user
        self.view = view
        self.update_ui_balance()
        self.signal_service()
        
    def signal_service(self):
        self.view.timer_signal.connect(lambda duration: 
                                       self.handle_pomodoro(duration))
    
    def handle_pomodoro(self, duration):
        duration=duration//60
        self.system.pomodoro_service(duration,self.user)
        self.update_ui_balance()

    def update_ui_balance(self):
        curr_balance= self.user.balance
        self.view.update_balance(curr_balance)
        print(f"user's balance updated.")
        print(f"current balance: {curr_balance}")
    
