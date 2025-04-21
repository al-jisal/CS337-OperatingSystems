class SolutionTwo:
    def __init__(self):
        self.flag = [False, False]

    def lock(self, thread_id):
        self.flag[thread_id - 1] = True
        print(self.flag)
        # add sleep here for context switching
        while self.flag[2 - thread_id]:
            continue

    def unlock(self, thread_id):
        self.flag[thread_id - 1] = False