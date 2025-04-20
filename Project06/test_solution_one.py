
import threading
from solution_one import SolutionOne


class Counter:
    def __init__(self):
        self.value = 0


    def increment(self):
            temp = self.value
            for _ in range(1000):  # waste some CPU cycles
                pass
            self.value = temp + 1


counter = Counter()


def worker_1(lock, id):
    for _ in range(700): # to test for progress, I reduced the range from 1000 to 700
        lock.lock(id)
        print(f"thread {id} in critical section")
        counter.increment()
        print(counter.value)
        lock.unlock(id)


def worker_2(lock, id):
    for _ in range(1000):
        lock.lock(id)
        print(f"thread {id} in critical section")
        counter.increment()
        print(counter.value)
        lock.unlock(id)


def main():
    lock = SolutionOne()
    t1 = threading.Thread(target=worker_1, args=(lock, 1, ))
    t2 = threading.Thread(target=worker_2, args=(lock, 2, ))


    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("Final counter value:", counter.value)



if __name__ == "__main__":
    main()