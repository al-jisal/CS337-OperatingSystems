import threading

class Semaphore:
    def __init__(self, counter=1):
        self.counter = counter
        self.condition = threading.Condition()

    def acquire(self):
        with self.condition:
            while self.counter <= 0:
                self.condition.wait()
            self.counter -= 1

    def release(self):
        with self.condition:
            self.counter += 1
            self.condition.notify()