import threading
import time
import random
from semaphore import Semaphore

class Buffer:
    
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.lock = threading.Lock()
        self.full = Semaphore(0)
        self.empty = Semaphore(self.size)
        
    def place(self, item):
        self.empty.acquire()
        
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        
        self.full.release()

        
    def remove(self):
        self.full.acquire()
        
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        
        self.empty.release()
        
        return item

my_buffer = Buffer(5)

def producer():
    for item in range(10000):
        print("adding item:", item, "\tbuffer length:", len(my_buffer.queue))
        my_buffer.place(item)



def producer(my_buffer):
    for item in range(10000):
        print("adding item:", item, "\tbuffer length:", len(my_buffer.queue))
        my_buffer.place(item)


def consumer(my_buffer):
    for index in range(10000):
        item = my_buffer.remove()
        print("removing item:", item, "\tbuffer length:", len(my_buffer.queue))


def main():
    my_buffer = Buffer(5)
    t1 = threading.Thread(target=producer, args=(my_buffer, ))
    t2 = threading.Thread(target=consumer, args=(my_buffer, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()