"""
import threading
import time
from solution_one import SolutionOne

x = 0


def increment():
    global x
    x += 1


def thread1_task(lock, my_num):
    global turn
   
    for _ in range(100000):
        lock.lock(my_num)
        time.sleep(0.0001)  # Simulate some work
        increment()
        print(x)
        lock.unlock(my_num)
        # put sleep here for testing progress
        # or asymetrical amount of iterations


def thread2_task(lock, my_num):
    global turn
   
    for _ in range(100000):
        lock.lock(my_num)
        print("Thread 2 in the critical section")
        increment()
        print(x)
        lock.unlock(my_num)


def main_task():
    global x


    x = 0
   
    # create a lock
    lock = SolutionOne()
    
    t1 = threading.Thread(target=thread1_task, args=(lock, 1, ))
    t2 = threading.Thread(target=thread2_task, args=(lock, 2, ))

       
    t1.start()
    t2.start()

    
    t1.join()
    print("i'm here")
    t2.join()
    


for i in range(2):
    main_task()
    print("Iteration {0}: x = {1}".format(i,x))
"""


import threading


class Counter:
    def __init__(self):
        self.value = 0


    def increment(self):
            temp = self.value
            for _ in range(1000):  # waste some CPU cycles
                pass
            self.value = temp + 1


counter = Counter()


def worker():
    for _ in range(1000):
        counter.increment()


threads = [threading.Thread(target=worker) for _ in range(10)]


for t in threads:
    t.start()


for t in threads:
    t.join()


print("Final counter value:", counter.value)

"""
for timing bounded wait time, put sleep statements in the lock implements
for timing progress, use asymetric number of iterations
"""