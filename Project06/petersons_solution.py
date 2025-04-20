class PetersonsSolution:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 1

    def lock(self, thread_id):
        self.flag[thread_id - 1] = True
        self.turn = 3 - thread_id
        while self.flag[2 - thread_id] and (self.turn == 3 - thread_id):
            continue

    def unlock(self, thread_id):
        self.flag[thread_id - 1] = False