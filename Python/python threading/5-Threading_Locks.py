from threading import Thread, Lock

a = 0
lock = Lock() # define thread lock (this can take some parameters)
def add():
    global a
    with lock:
        for _ in range(100_000):
            # print('adding 2\n')
            a += 5

def subtract_3():
    global a
    with lock:
        for _ in range(100_000):
            # print('subtracting 1\n')
            a -= 3

def subtract_2():
    global a
    with lock: # this makes sure only this thread can operate on the variable until it finishes
        for _ in range(100_000):
            # print('subtracting 1\n')
            a -= 2


adder = Thread(target=add())
subtractor1 = Thread(target=subtract_3())
subtractor2 = Thread(target=subtract_2())

adder.start()
subtractor1.start()
subtractor2.start()

adder.join()
subtractor1.join()
subtractor2.join()

print(f'\n final value : {a}')
