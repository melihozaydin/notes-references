#Threading module

import threading
import time

def sleeper(n,name):
    print(f'Hi I am {name}. Going to sleep for {n} seconds.\n')
    time.sleep(n)
    print(f'{name} has woken up from sleep \n')


thread_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name=f'thread{i}', args= (5, f'thread{i}') )
    thread_list.append(t)
    t.start()
    print()

for t in thread_list:
    t.join()

end = time.time()

print(f'time taken {end-start}')