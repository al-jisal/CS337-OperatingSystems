"""This contains a function that computes the sum of squares for 
   a range of numbers in a parallelism(multiprocessing) manner
"""
import os
import time
import multiprocessing

def sum_of_squares(n):
    """Computes the sum of squares in the range of n"""
    print(f'{os.getpid()} is running')
    return sum([i * i for i in range(n)])


def main():
    """Main Function"""
    N = 10**7                   # Large number for heavy computation
    processes = {}              # a dictionary for holding the processes
    start_time = time.time()

    print(f'parent process id: {os.getpid()}\n')

    # creates the processes
    for i in range(4):
        processes[f'process{i}'] = multiprocessing.Process(target=sum_of_squares, args=(N,))

    # starts the processes(think of it as the processes join the wait queue)
    for name, process in processes.items():
        process.start()
        print(f'{name} started with id: {process.pid}')
    print()

    # wait until all processes are finished executin
    for process in processes.values():
        process.join()
    print()

    # checks if all processes are done
    for name, process in processes.items():
        print(f'Is {process.pid} still running: {process.is_alive()}')
    print()
    
    end_time = time.time()
    print("Parallel Execution Time:", end_time - start_time)


if __name__ == "__main__":
    main()
