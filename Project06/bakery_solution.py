import time

class BakerySolution:
    def __init__(self, thread_count):
        self.thread_count = thread_count
        self.choosing = [False] * thread_count
        self.tickets = [0] * thread_count

    def lock(self, thread_id):
        self.choosing[thread_id - 1] = True
        self.tickets[thread_id - 1] = max(self.tickets) + 1
        # time.sleep(0.0001) # this induces context switch for testing bounded wait time
        self.choosing[thread_id - 1] = False

        for i in range(self.thread_count):
            while self.choosing[i]:
                continue
            while (self.tickets[i] != 0 and
                   ((self.tickets[i], i) < (self.tickets[thread_id - 1], thread_id - 1))):
                continue

    def unlock(self, thread_id):
        self.tickets[thread_id - 1] = 0
        