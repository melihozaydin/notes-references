import queue

# First in First Out (FIFO) queue
q = queue.Queue()

q.put(5)
q.put(6)

print(q.get(), q.get(), 'is_empty:', q.empty())

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end='  ')

"""
https://www.youtube.com/watch?v=wkPMom77Hqk&list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm&index=8

if you try to q.get from an empty queue program will block (freeze) and wait until it has an element
that is why you usualy have one thread put in items and another wait for them to come in and seperately process them 
"""

import threading
import time

def putting_thread(q):
    while True:
        print('Starting Thread')
        time.sleep(5)
        q.put(5)
        print('put something')

q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,),daemon=True)

t.start()

q.put(2)
print(q.get())
print('firts item gotten')
print(q.get())
print('finished')
