"""
    Name: Desmond Frimpong
    Course: CS337
    Project: 5
    Date: 04/07/2025
    File: multitasking_code.py

    This is  a program to process eight years of Reddit comments to find the total word count
    and the frequency of each word in each year and collectively. This program uses creative 
    multitasking skills to speed up the code
"""

from multiprocessing import Pool, cpu_count
import os, re, time
from collections import Counter

def process_file(file_path):
    start = time.time()
    word_count = 0
    word_freq = Counter()

    print(f"Processing {os.path.basename(file_path)} ...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                words = re.findall(r"\b[\w']+\b", line.lower())
                word_freq.update(words)
                word_count += len(words)
    except Exception as e:
        return file_path, Counter(), 0, 0.0

    duration = time.time() - start
    return file_path, word_freq, word_count, duration

def main():
    start_time = time.time()
    base_dir = os.path.dirname(__file__)
    files = [f'reddit_comments_{y}.txt' for y in range(2008, 2016)]
    file_paths = [os.path.join(base_dir, "Reddit Comments", f) for f in files]

    per_file_performance = {}

    with Pool(processes=cpu_count()) as pool:
        results = [pool.apply_async(process_file, args=(fp,)) for fp in file_paths]

        for i, result in enumerate(results):
            try:
                file_path, word_counter, word_count, duration = result.get(timeout=60)
                filename = os.path.basename(file_path)
                print(f"\nTime taken to process {filename}: {duration:.2f} seconds")
                print(f"Total words in {filename}: {word_count}")
                print("-" * 80 + "\n")
                per_file_performance[filename] = duration
            except Exception as e:
                print(f"[ERROR] Processing {os.path.basename(file_paths[i])} failed: {e}")

    total_duration = time.time() - start_time
    print(f"Total Time Taken: {total_duration:.2f} seconds")
    return per_file_performance, total_duration

if __name__ == "__main__":
    main()
