import threading
import time


    
class Timer:
    def __init__(self,duration=25):
        self.duration=duration*60
        self.remaining_time = 0
        self.timer_thread = threading.Thread(target=self.run_timer)
        self.timer_thread.daemon = True #allowing to close the app even if the
        #thread is still running

    def run_timer(self):
        while self.remaining_time>0:
            self.remaining_time-=1
            time.sleep(1)
    
    def start(self):
        if not self.timer_thread.is_alive():
            self.remaining_time=self.duration
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()