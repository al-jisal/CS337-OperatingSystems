
import threading
from extension import FilterLock


class Counter:
    def __init__(self):
        self.value = 0


    def increment(self):
            temp = self.value
            for _ in range(1000):  # waste some CPU cycles
                pass
            self.value = temp + 1


counter = Counter()


def worker(lock, id):
    for _ in range(1000):
        lock.lock(id)
        print(f"thread {id} in critical section")
        counter.increment()
        print(counter.value)
        lock.unlock(id)


def main():
    lock = FilterLock(5)
    t1 = threading.Thread(target=worker, args=(lock, 1, ))
    t2 = threading.Thread(target=worker, args=(lock, 2, ))
    t3 = threading.Thread(target=worker, args=(lock, 3, ))
    t4 = threading.Thread(target=worker, args=(lock, 4, ))
    t5 = threading.Thread(target=worker, args=(lock, 5, ))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


    print("Final counter value:", counter.value)



if __name__ == "__main__":
    main()