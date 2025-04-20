
import threading
import solution_one


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


def worker():
    for _ in range(1000):
        counter.increment()


def main():
    threads = [threading.Thread(target=worker) for _ in range(10)]


    for t in threads:
        t.start()


    for t in threads:
        t.join()


    print("Final counter value:", counter.value)



if __name__ == "__main__":
    main()