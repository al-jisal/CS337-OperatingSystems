"""
In this file,
    - processes are created 
    - scheduler runs
    - statistics are calculated
"""
import pandas as pd
import scheduler

def kernel(selected_scheduler, processes, verbose=True):
    """Simulates CPU scheduling aspect of an operating system kernel"""
    CPU, ready, time = [],[], 0

    scheduler.add_ready(processes, ready, time)

    while ready:
        time = selected_scheduler(processes, ready, CPU, time)

    wait_times, turnaround_times = [], []
    for item in processes:
        wait_times.append(item.wait_time)
        turnaround_times.append(item.turnaround_time)

    df = pd.DataFrame(CPU)
    df["wait time"] = wait_times
    df["turnaround time"] = turnaround_times
    df.to_csv("results.csv", index=False)

    average_wait_time = df["wait time"].mean(axis=0)
    average_turnaround_time = df["turnaround time"].mean(axis=0)
    return average_wait_time, average_turnaround_time

