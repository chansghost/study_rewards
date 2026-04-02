from user import User

class System:
    def __init__(self):
        #loading config from file/creating it
        self.tasks=[]
        time=5
        self.times_pomodoro=[]
        self.pomodoro_payout=[]
        for i in range(12):
            time=time*i
            self.times_pomodoro.append(time)
            self.pomodoro_payout.append(i)
        
        
    
    def pomodoro_service(self, duration, user):
        #you get 1 coin for each 5 mins of pomodoro
        index = self.times_pomodoro.index(duration)
        coins = self.pomodoro_payout[index]
        user.add_coins(coins)
    
    
    def rewards_service(self):
        pass
