class FilterLock:
    def __init__(self, n):
        self.n = n
        self.level = [0] * (n+1)    # 1‑indexed
        self.victim = [None] * (n+1)  # victim[1..n‑1]

    def lock(self, i):
        # climb from stage 1 up to N‑1
        for k in range(1, self.n):
            self.level[i]   = k
            self.victim[k] = i
            # wait while any other thread is at ≥ my level
            # AND I’m still the victim for this level
            while any(
                j != i
                and self.level[j] >= k
                and self.victim[k] == i
                for j in range(1, self.n+1)
            ):
                pass

    def unlock(self, i):
        self.level[i] = 0
