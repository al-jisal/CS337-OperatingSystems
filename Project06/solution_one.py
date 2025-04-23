class SolutionOne:
    """
    A simle implementation of a lock using a turn variable.
    """
    def __init__(self):
        self.turn = 1

    def lock(self, thread_id):
        while self.turn != thread_id:
            continue

    def unlock(self, thread_id):
        self.turn = 3 - thread_id
            