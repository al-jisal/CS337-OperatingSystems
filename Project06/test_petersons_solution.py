
import threading
import time
from petersons_solution import PetersonsSolution


class Counter:
    def __init__(self):
        self.value = 0


    def increment(self):
            temp = self.value
            for _ in range(1000):  # waste some CPU cycles
                pass
            self.value = temp + 1


counter = Counter()


def worker(lock, id, iteration):
    for _ in range(iteration):  
        lock.lock(id)
        # print(f"thread {id} in critical section")
        counter.increment()
        # print(counter.value)
        lock.unlock(id)


# def worker_2(lock, id):
#     for _ in range(1000):
#         lock.lock(id)
#         print(f"thread {id} in critical section")
#         counter.increment()
#         print(counter.value)
#         lock.unlock(id)

def test_n_thread_mutual_exclusion():
    lock = PetersonsSolution()
    t1 = threading.Thread(target=worker, args=(lock, 1, 1000, ))
    t2 = threading.Thread(target=worker, args=(lock, 2, 1000, ))
    t3 = threading.Thread(target=worker, args=(lock, 3, 1000, ))


    threads = [t1, t2, t3]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    print("Final counter value:", counter.value)
     

def main():
    test_n_thread_mutual_exclusion()



if __name__ == "__main__":
    main()