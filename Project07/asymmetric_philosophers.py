"""
Name: Desmond Frimpong
Course: CS337
Project: 7
Date: 04/14/2025
File: asymmetric_philosophers.py

This file solves the dining philosophers' problem using the asymmetric approach
"""

import random, time, threading
from semaphore import Semaphore

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, iterations=5):
        super().__init__()
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.iterations = iterations

    def run(self):
        for _ in range(self.iterations):
            print(f"P{self.index} is thinking...")
            time.sleep(random.uniform(0.2, 0.6))

            # Asymmetric: even -> left then right; odd -> right then left
            if self.index % 2 == 0:
                print(f"P{self.index} is taking left fork...")
                self.left_fork.acquire()
                time.sleep(0.1)
                print(f"P{self.index} is taking right fork...")
                self.right_fork.acquire()
            else:
                print(f"P{self.index} is taking right fork...")
                self.right_fork.acquire()
                time.sleep(0.1)
                print(f"P{self.index} is taking left fork...")
                self.left_fork.acquire()

            print(f"P{self.index} is eating...")
            time.sleep(random.uniform(0.2, 0.6))

            print(f"P{self.index} dropped right fork...")
            self.right_fork.release()
            print(f"P{self.index} dropped left fork...")
            self.left_fork.release()

        print(f"P{self.index} is done eating!")
        


def dining_philosophers(num_philosophers=5):
    forks = []
    philosophers = []

    for i in range(num_philosophers):
        forks.append(Semaphore(1))

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosophers.append( Philosopher(i, left_fork, right_fork) )

    for p in philosophers:
        p.start()
        time.sleep(0.05)

    for p in philosophers:
        p.join()


def main():
    dining_philosophers()

    
if __name__ == "__main__":
    main()