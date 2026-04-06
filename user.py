import json
import os.path

pomodoro_times = 12 #12 possible times, starting from 5 mins to 60 mins

class User:
    def __init__(self, name = "unknown"):
        self.name=name
        self.pomodoro_counter=[0 for i in range(pomodoro_times)]
        #storage for all the pomodoros that the user completed
        self.balance=0
        self.load_user()
    
    def load_user(self):
        if os.path.exists('user.json'):
            with open('user.json', 'r') as f:
                data = json.load(f)

                self.name= data.get("name", "john doe")
                self.pomodoro_counter = data.get("pomodoro_count", 0)
                self.balance = data.get("balance", 0)

                print(f"loaded user {self.name}, balance: {self.balance}")
        else:
            self.save_user()
        
    
    def save_user(self):
        data = {
            "name": self.name,
            "pomodoro_count": 0,
            "balance": self.balance
        }

        with open(f'user.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"saved user {self.name}")

    def add_coins(self, amount):
        self.balance+=amount
        print(f"added {amount} coins to the account")
        self.save_user()

    