pomodoro_times = 12 #12 possible times, starting from 5 mins to 60 mins

class User:
    def __init__(self, name = "unknown"):
        self.name=name
        self.pomodoro_counter=[0 for i in range(pomodoro_times)]
        #storage for all the pomodoros that the user completed
        self.balance=0
    
    def load_user(self):
        #loads user settings, name, balance etc
        pass
    
    def add_coins(self, amount):
        self.balance+=amount
    
    def get_balance(self):
        return self.balance
    