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

    wait_times, turnaround_times = [], []
    for item in processes:
        wait_times.append(item.wait_time)
        turnaround_times.append(item.turnaround_time)

    df = pd.DataFrame(CPU)
    df["wait time"] = wait_times
    df["turnaround time"] = turnaround_times
    df.to_csv(filename, index=False)

    average_wait_time = df["wait time"].mean(axis=0)
    average_turnaround_time = df["turnaround time"].mean(axis=0)
    return average_wait_time, average_turnaround_time
