#Threading module

import threading
import time

def sleeper(n,name):
    print(f'Hi I am {name}. Going to sleep for {n} seconds.\n')
    time.sleep(n)
    print(f'{name} has woken up from sleep \n')

# this sets up the thread
t = threading.Thread(target=sleeper, name='thread1', args= (5, 'thread1') )

t.start()  # this starts the thread

"""
Main thread will keep printing while thread 1 is waiting 5 seconds
t.join tells the main thread to wait for thread1 to finish its process
"""
t.join()

print('Main Thread has started')
