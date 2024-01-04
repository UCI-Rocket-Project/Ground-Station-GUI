import sys
import time

def global_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        sys.__excepthook__(exctype, value, traceback)
    else:
        print('Failed with exception')
        print(value, traceback)

sys.excepthook = global_hook

start_time = time.time()
wait_time = 5 #seconds

while True:
    if time.time() - start_time > wait_time:
        raise IOError('we must test excepthook')


