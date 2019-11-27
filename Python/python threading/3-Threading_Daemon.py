import threading
import time

total = 4

def create_items():
    global total
    for _ in range(100):
        time.sleep(.2)
        print('added item')
        total += 1
    print('creation is done')

def create_items_2():
    global total
    for _ in range(70):
        time.sleep(0.1)
        print('added item')
        total += 1
    print('creation is done')

def limit_items():

    global total
    while True:
        if total > 5:
            
            print('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(0.05)
            print('Waiting')


"""
the problem with this code is that limiter thread is an infinite loop so even when the creator threads finish and we return to the main thread and print the final total
waiting promt will not end so we cant exit the program.

this is where Daemon threads come in,

daemon thread will end itself when the main program ends.
"""

creator1 = threading.Thread(target=create_items)
creator2 = threading.Thread(target=create_items_2)
limiter = threading.Thread(target=limit_items, daemon=True)  # we define limiter as a daemon thread
print('limiter is daemon : ', limiter.isDaemon())

creator1.start()
creator2.start()
limiter.start()

creator1.join()
creator2.join()

# this will block the main thread from continuing and program will get stuck
# because daemon thread waits for the main program(thread) to finish
#limiter.join() 

print(f'our final total is {total}')


