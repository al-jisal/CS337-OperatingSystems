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
                   quantum=None, # max time slices that each process get to run
                   verbose=True):
    """non-preemptive First Come First Serve(FCFS) scheduler"""
    process = find_lowest_arrival(ready)
    response(process, time)
    process.set_wait_time(time - process.get_arrival_time())
    start_time = time
    duty = process.get_duty()
    burst_time = duty[0]

    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    duty[0] = 0
    process.set_duty(duty)
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
                  quantum=None,
                  verbose=True):
    """non-preemptive Shortest Job First(SJF) scheduler"""
    heap = [(item.get_duty()[0], item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    response(process, time)
    process.set_wait_time(time - process.get_arrival_time())
    ready.remove(process)
    start_time = time
    duty = process.get_duty()
    burst_time = duty[0]
    
    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    duty[0] = 0
    process.set_duty(duty)
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
                       quantum=None,
                       verbose=True):
    """non-preemptive Priority scheduler"""
    heap = [(-item.get_priority(), item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    response(process, time)
    process.set_wait_time(time - process.get_arrival_time())
    ready.remove(process)
    start_time = time
    duty = process.get_duty()
    burst_time = duty[0]
    
    while burst_time > 0:
        burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    duty[0] = 0
    process.set_duty(duty)
    process.set_turnaround_time(time - process.get_arrival_time())
    end_time = time
    CPU.append( dict(process=process.get_ID(),
                     Start=start_time,
                     Finish=end_time,
                     Priority=process.get_priority()))
    return time


def RR_scheduler(processes,
                 ready,
                 CPU,
                 time,
                 quantum,
                 verbose=True):
    """a preemptive on quantum First Come First Serve (Round Robin) scheduler"""
    process = find_lowest_arrival(ready)
    response(process, time)
    process.set_wait_time(process.get_wait_time() + (time - process.get_arrival_time()))
    process.set_status("running")
    start_time = time

    while quantum > 0 and process.get_duty()[0] > 0:
        quantum -= 1
        time += 1
        duty = process.get_duty()
        duty[0] -= 1
        process.set_duty(duty)
        add_ready(processes, ready, time)

    if process.get_duty()[0] > 0:
        process.set_arrival_time(time)
        process.set_status("waiting")
        ready.append(process)
    else:
        process.set_turnaround_time(process.get_wait_time() + (time - process.get_arrival_time()))
    CPU.append( dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=time,
                    Priority=process.get_priority()))

    return time

# ----------------------------- Helper Functions ------------------------------------------------------

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

def response(process, time):
    """sets the response time for a process"""
    if process.get_wait_time() == 0:
        process.set_response_time(time - process.get_arrival_time())