"""
In this file,
    - processes are created 
    - scheduler runs
    - statistics are calculated
"""
import pandas as pd
import process, scheduler

def kernel(selected_scheduler, verbose=True):
    """Simulates CPU scheduling aspect of an operating system kernel"""
    CPU, ready, processes, time = [], [], [], 0

    # creating processes
    process0 = process.Process(0, 5, 0, 30)
    process1 = process.Process(1, 4, 2, 35)
    process2 = process.Process(2, 1, 5, 36)
    process3 = process.Process(3, 6, 6, 20)

    processes.append(process0)
    processes.append(process1)
    processes.append(process2)
    processes.append(process3)

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

