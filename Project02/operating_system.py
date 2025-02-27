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

def kernel(selected_scheduler, processes, filename, quantum=None, levels=None, verbose=True):
    """Simulates CPU scheduling aspect of an operating system kernel"""
    CPU, time = [], 0
    completed = 0

    if selected_scheduler == scheduler.MFQ_scheduler:
        first_queue, second_queue, third_queue, waiting_queue = [], [], [], []
        scheduler.add_ready(processes, first_queue, time)

        while completed < len(processes):
            if first_queue or second_queue or third_queue or waiting_queue:
                time = selected_scheduler(processes,
                                          first_queue,
                                          second_queue,
                                          third_queue,
                                          waiting_queue,
                                          CPU,
                                          time,
                                          levels)
                completed = sum([len(item.get_duty()) == 0 for item in processes])
            else:
                time += 1
                scheduler.add_ready(processes, first_queue, time)
    else:
        ready = []

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
    dp = pd.DataFrame()
    dp["processes"] = processes
    dp["response time"] = response_times
    dp["wait time"] = wait_times
    dp["turnaround time"] = turnaround_times
    df.to_csv(filename, index=False)

    return dp
