"""
    Name: Desmond Frimpong
    Course: CS337
    Project: 5
    Date: 04/07/2025
    File: serial_code.py

    This is  a program to process eight years of Reddit comments to find the total word count
    and the frequency of each word in each year and collectively. The program implements a base
    version of the code that does not use any multitasking concepts to speed up the code. This 
    program is used as a base-line for comparison.
"""
import os
import re
from collections import Counter
import time

def process_file(file_path):
    """
    Reads a file and returns a dictionary with the frequency of each word,
    normalized to lowercase and stripped of punctuation.
    
    :param file_path: Path to the file to be read.
    :return: a tupple of Counter of words and total words in file.
    """
    all_words, total_words = [], 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Use regex to extract words (alphanumeric and apostrophes)
                words = re.findall(r"\b[\w']+\b", line.lower())
                all_words.extend(words)
                total_words += len(words)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return Counter(), 0
    
    return Counter(all_words), total_words

def main():
    """
    Main function to process Reddit comments and calculate word frequencies.
    """
    start_time = time.time()
    base_dir = os.path.dirname(__file__)
    per_file_performance = {}

    files = [
        'reddit_comments_2008.txt',
        'reddit_comments_2009.txt',
        'reddit_comments_2010.txt',
        'reddit_comments_2011.txt',
        'reddit_comments_2012.txt',
        'reddit_comments_2013.txt',
        'reddit_comments_2014.txt',
        'reddit_comments_2015.txt'
    ]

    for file in files:
        file_start_time = time.time()
        file_path = os.path.join(base_dir, "Reddit Comments", file)

        print(f"\nProcessing {file} ...")
        word_counts, total_words = process_file(file_path)

        file_end_time = time.time()
        per_file_performance[file] = file_end_time - file_start_time

        print(f"Time taken to process {file}: {per_file_performance[file]:.2f} seconds")
        print(f"Total words in {file}: {total_words}")
        print("-" * 40)

    total_duration = time.time() - start_time
    print(f"Total Time Taken: {total_duration:.2f} seconds")
    
    return per_file_performance, total_duration

if __name__ == "__main__":
    main()