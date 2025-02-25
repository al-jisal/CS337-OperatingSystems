"""
Name: Desmond Frimpong
Course: CS337
Project: 2
Date: 02/26/2025
File: operating_system.py

In this file,
    - processes are created 
    - scheduler runs
    - statistics are calculated
"""
import pandas as pd
import scheduler

def kernel(selected_scheduler, processes, filename, quantum=None, verbose=True):
    """Simulates CPU scheduling aspect of an operating system kernel"""
    CPU, ready, time = [],[], 0
    completed = 0

    scheduler.add_ready(processes, ready, time)

    while completed < len(processes):
        if ready:
            time = selected_scheduler(processes, ready, CPU, time, quantum)
            completed = sum([item.get_duty()[0] == 0 for item in processes])
        else:
            time += 1
            scheduler.add_ready(processes, ready, time)

    response_times, wait_times, turnaround_times = [], [], []
    for item in processes:
        response_times.append(item.get_response_time())
        wait_times.append(item.get_wait_time())
        turnaround_times.append(item.get_turnaround_time())

    df = pd.DataFrame(CPU)
    df["response time"] = response_times
    df["wait time"] = wait_times
    df["turnaround time"] = turnaround_times
    df.to_csv(filename, index=False)

    average_response_time = df["response time"].mean(axis=0)
    average_wait_time = df["wait time"].mean(axis=0)
    average_turnaround_time = df["turnaround time"].mean(axis=0)
    return average_response_time, average_wait_time, average_turnaround_time
