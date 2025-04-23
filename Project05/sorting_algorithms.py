"""
    Name: Desmond Frimpong
    Course: CS337
    Project: 5
    Date: 04/07/2025
    File: sorting_algorithms.py
"""
import time
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
import pandas as pd


def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Sorts an array using the selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Find the minimum element in remaining unsorted array
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# parallel versions of sorting algorithms
def parallel_sort(arr, sort_function, num_processes=None):
    """
    Parallelize a sorting algorithm by splitting the array,
    sorting subarrays, and then merging them.
    
    params:
        arr: Array to sort
        sort_function: The sorting function to use
        num_processes: Number of processes to use (defaults to CPU count)
    
    Returns:
        Sorted array
    """
    if num_processes is None:
        num_processes = mp.cpu_count()
    
    # use sequential sort if array is small or only one process
    if len(arr) <= 1000 or num_processes <= 1:
        return sort_function(arr.copy())
    
    # split array into chunks for parallel processing
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    
    # create a pool of workers and sort each chunk
    with mp.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(sort_function, chunks)
    
    # merge the sorted chunks
    result = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        result = merge(result, chunk)
    
    return result


def measure_sorting_performance(arr, sizes, algorithms, parallel=False, num_processes=None):
    """
    Measure the performance of sorting algorithms on different array sizes.
    
    params:
        arr: Original large array to sample from
        sizes: List of array sizes to test
        algorithms: Dictionary mapping algorithm names to functions
        parallel: Whether to use parallel version
        num_processes: Number of processes for parallel sorting
    
    Returns:
        DataFrame with performance results
    """
    results = []
    
    for size in sizes:
        # sample from the original array
        sample = np.random.choice(arr, size=size, replace=False)
        
        for name, func in algorithms.items():
            test_arr = sample.copy()
            
            start_time = time.time()
            
            if parallel:
                sorted_arr = parallel_sort(test_arr, func, num_processes)
            else:
                sorted_arr = func(test_arr)
                
            end_time = time.time()
            execution_time = end_time - start_time
            
            
            results.append({
                'algorithm': name,
                'array_size': size,
                'execution_time': execution_time
            })
    
    return pd.DataFrame(results)


def save_and_plot_results(sequential_df, parallel_df):
    """
    Save results to CSV and create comparison plots.
    
    params:
        sequential_df: DataFrame with sequential sorting results
        parallel_df: DataFrame with parallel sorting results
    """

    sequential_df.to_csv('sequential_sorting.csv', index=False)
    parallel_df.to_csv('parallel_sorting.csv', index=False)
    
    plt.figure(figsize=(12, 8))
    
    # plot execution time vs array size for each algorithm (sequential vs parallel)
    for algorithm in sequential_df['algorithm'].unique():
        sequential_data = sequential_df[sequential_df['algorithm'] == algorithm]
        parallel_data = parallel_df[parallel_df['algorithm'] == algorithm]
        
        plt.plot(sequential_data['array_size'], sequential_data['execution_time'], 
                 marker='o', label=f'{algorithm} (Sequential)')
        plt.plot(parallel_data['array_size'], parallel_data['execution_time'], 
                 marker='x', linestyle='--', label=f'{algorithm} (Parallel)')
    
    plt.title('Performance Chart for Sorting Algorithms ')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.xscale('log')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # save the plot to root directory
    plt.savefig('sorting_performance_comparison.png')
    plt.close()


def main():
    # set random seed for reproducibility
    np.random.seed(42)
    
    # create a large array of random numbers
    array_size = 100000
    original_array = np.random.randint(0, 1000000, size=array_size)
    
    # define the sorting algorithms to test
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort
    }
    
    # Define array sizes to test
    # Using smaller sizes because these algorithms are O(n²)
    sizes = [100, 500, 1000, 5000, 10000]
    
    # get the number of available CPU cores
    num_processes = mp.cpu_count()
    print(f"\nNumber of CPU cores available: {num_processes}")
    
    # measure sequential performance
    print("\nMeasuring sequential sorting performance...")
    sequential_results = measure_sorting_performance(
        original_array, sizes, algorithms, parallel=False
    )
    
    # measure parallel performance
    print("\nMeasuring parallel sorting performance...")
    parallel_results = measure_sorting_performance(
        original_array, sizes, algorithms, parallel=True, num_processes=num_processes
    )
    
    # save results and create plots
    save_and_plot_results(sequential_results, parallel_results)
    print("\nDone")
    
if __name__ == '__main__':
    main() 