import threading
import time

MINUTES=True
SECONDS=False

class Timer:
    def __init__(self,duration=25):
        self.duration=self.convert_time(duration, MINUTES)
        

    def convert_time(self, duration_to_convert, unit):
        if unit==MINUTES:
            duration=duration_to_convert*60
            return duration
        if unit==SECONDS:
            duration=duration_to_convert/60
            return duration