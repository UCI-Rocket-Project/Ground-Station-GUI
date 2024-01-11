from threading import Thread, Lock
import time

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
        self.t.start()
        
    def stop(self):
        self.is_running = False
        self.t.join()


class ECUConnection:
    def __init__(self):
        self.lock = Lock()
        
    def get_data(self):
        with self.lock:


if __name__ == "__main__":
    def just_print():
        print("print")
    l = LoopThread(just_print)
    l.loop(2)
    time.sleep(5)
    l.stop()