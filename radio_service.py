from threading import Thread, Lock
import time
import math
import random

class LoopThread:
    ''' Basic Loop thread to spin off a thread and run a function any number of times for any given interval'''
    def __init__(self, func):
        self.mutex = Lock()
        self.is_running = False
        self.func = func

    def loop(self, sleep_time=0):
        self.is_running = True
        def threading_func():
            while self.is_running:
                self.func()
                time.sleep(sleep_time)
        self.t = Thread(target=threading_func)
        self.t.daemon = True
        self.t.start()
        
    def stop(self):
        self.is_running = False
        self.t.join()


class ECUConnection:
    def __init__(self):
        self.lock = Lock()
        self.data = {
            "pt": [0,0,0],
            "tc":[0,0,0],
            "solenoid":[0,0,0]
        }
        def rando_change():
            key = ["pt","tc","solenoid"][random.randint(0,2)]
            index = random.randint(0,2)
            val = random.randint(0,2)
            self.set_data(key,index,val)
        self.t = LoopThread(rando_change)
        self.t.loop(5)

    def get_data(self):
        with self.lock:
            return self.data
        
    def set_data(self, key, index, val):
        print(key,index,val)
        with self.lock:
            self.data[key][index] = val


if __name__ == "__main__":
   ecu = ECUConnection()
   while True:
       print(ecu.get_data())
       time.sleep(0.5)