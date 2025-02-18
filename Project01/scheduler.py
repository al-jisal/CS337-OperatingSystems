"""
The scheduler contains programs for scheduling processes on the CPU
"""
def FCFS_scheduler(processes, # list of all the processes in the simulation, whether arrived or not
                   ready, # list of processes with current arrival time
                   CPU, # list that holds beginnig and end runtimes for each process
                   time, # an integer representing the current time
                   verbose=True):
    """non-preemptive First Come First Serve(FCFS) scheduler"""
    process = find_lowest_arrival(ready)
    process.wait_time = time - process.arrival_time
    start_time = time

    while process.burst_time > 0:
        process.burst_time -= 1
        time += 1
        add_ready(processes, ready, time)

    process.turnaround_time = time - process.arrival_time
    end_time = time
    CPU.append( dict(process=process.get_ID(),
                     Start=start_time,
                     Finish=end_time,
                     Priority=process.get_priority()))
    return time


def SJF_scheduler(processes,
                  CPU,
                  time,
                  verbose=True):
    """non-preemptive Shortest Job First(SJF) scheduler"""
    # keep a ready heap of tupples (process, burst_time)
    # pick process with lowest arrival to run 
    # set start time to time


def Priority_scheduler(processes,
                       CPU,
                       time,
                       verbose=True):
    """non-preemptive Priority scheduler"""
    # keep a ready heap of tupples (process, priority)


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