"""
Name: Desmond Frimpong
Course: CS337
Project: 2
Date: 02/26/2025
File: scheduler.py
The scheduler contains programs for scheduling processes on the CPU
"""
import heapq

def FCFS_scheduler(processes, # list of all the processes in the simulation, whether arrived or not
                   ready, # list of processes with current arrival time
                   CPU, # list that holds beginnig and end runtimes for each process
                   time, # an integer representing the current time
                   verbose=True):
    """non-preemptive First Come First Serve(FCFS) scheduler"""
    process = find_lowest_arrival(ready)
    process.set_wait_time(time - process.get_arrival_time())
    start_time = time
    burst_time = process.get_burst_time()

    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    process.set_turnaround_time(time - process.get_arrival_time())
    end_time = time
    CPU.append( dict(process=process.get_ID(),
                     Start=start_time,
                     Finish=end_time,
                     Priority=process.get_priority()))
    return time


def SJF_scheduler(processes,
                  ready,
                  CPU,
                  time,
                  verbose=True):
    """non-preemptive Shortest Job First(SJF) scheduler"""
    heap = [(item.get_burst_time(), item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    process.set_wait_time(time - process.get_arrival_time())
    ready.remove(process)
    start_time = time
    burst_time = process.get_burst_time()
    
    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    process.set_turnaround_time(time - process.get_arrival_time())
    end_time = time
    CPU.append( dict(process=process.get_ID(),
                     Start=start_time,
                     Finish=end_time,
                     Priority=process.get_priority()))
    return time


def Priority_scheduler(processes,
                       ready,
                       CPU,
                       time,
                       verbose=True):
    """non-preemptive Priority scheduler"""
    heap = [(-item.get_priority(), item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    process.set_wait_time(time - process.get_arrival_time())
    ready.remove(process)
    start_time = time
    burst_time = process.get_burst_time()
    
    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    process.set_turnaround_time(time - process.get_arrival_time())
    end_time = time
    CPU.append( dict(process=process.get_ID(),
                     Start=start_time,
                     Finish=end_time,
                     Priority=process.get_priority()))
    return time


def find_lowest_arrival(ready):
    """returns the process with the lowest arrival time in the ready queue"""
    if len(ready) == 0:
        return None
    
    process = None
    process_arrival_time = float("inf")
    for item in ready:
        if item.arrival_time < process_arrival_time:
            process = item
            process_arrival_time =item.arrival_time
    ready.remove(process)
    return process


def add_ready(processes, ready, time):
    """adds processes arriving at the current time to the ready queue"""
    for process in processes:
        if process.get_arrival_time() == time:
            ready.append(process)
