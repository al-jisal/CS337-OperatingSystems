"""This contains a function that computes the sum of squares
   for a range of numbers in a sequential manner
"""

import time


def sum_of_squares(n):
    """Computes the sum of squares in the range of n"""
    return sum([i * i for i in range(n)])


def main():
    """Main Function"""
    N = 10**7  # Large number for heavy computation
    start_time = time.time()
   
    results = [sum_of_squares(N) for _ in range(4)]   
    end_time = time.time()
    print("Sequential Execution Time:", end_time - start_time)


if __name__ == "__main__":
    main()
