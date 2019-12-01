import threading
import time
import random

# events are used for signaling between threads
"""
event = threading.Event()

event.set()
event.clear()

print('even state =', event.is_set())

event.wait() # this will wait until event.is_set()
"""

def flag():
    time.sleep(3)
    event.set()
    print('starting countdown')
    time.sleep(7)
    print('coundown finished event cleared')
    event.clear()

def start_ops():
    event.wait()

    while event.is_set():
        print('\nstarting random int task')
        x = random.randint(1,30)
        time.sleep(5)
        if x <= 29:
            print('x <= 29 !!!')
    print('event has stopped, random int operation stopped')

event = threading.Event()

t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_ops)

t1.start()
t2.start()