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


def SRT_scheduler(processes,
                  ready,
                  CPU,
                  time,
                  quantum=None,
                  verbose=True):
    """a preemptive on arrival Shortest Job First (Shortest Remaining Time) scheduler"""
    heap = [(item.get_duty()[0], item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    ready.remove(process)
    response(process, time)
    process.set_wait_time(process.get_wait_time() + (time - process.get_arrival_time()))
    process.set_status("running")
    start_time = time
    queue_length = len(ready)

    while (
            ((len(heap) > 0 and process.get_duty()[0] < heap[0][2].get_duty()[0])
             or process.get_duty()[0]> 0
            )
            and process.get_duty()[0]> 0 ):
        time += 1
        duty = process.get_duty()
        duty[0] -= 1
        process.set_duty(duty)
        add_ready(processes, ready, time)
        if len(ready) > queue_length:
            heap = [(item.get_duty()[0], item.get_ID(), item) for item in ready]
            heapq.heapify(heap)
            queue_length = len(ready)

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


def PP_scheduler(processes,
                 ready,
                 CPU,
                 time,
                 quantum=None,
                 verbose=True):
    """a preemptive on arrival Priority (Preemptive Priority) scheduler"""
    heap = [(-item.get_priority(), item.get_ID(), item) for item in ready]
    heapq.heapify(heap)
    _, _, process = heapq.heappop(heap)
    ready.remove(process)
    response(process, time)
    process.set_wait_time(process.get_wait_time() + (time - process.get_arrival_time()))
    process.set_status("running")
    start_time = time
    queue_length = len(ready)

    while (process.get_duty()[0] > 0 and 
           (len(heap) == 0 or process.get_priority() > heap[0][2].get_priority())
        ):
        time += 1
        duty = process.get_duty()
        duty[0] -= 1
        process.set_duty(duty)
        add_ready(processes, ready, time)
        if len(ready) > queue_length:
            heap = [(-item.get_priority(), item.get_ID(), item) for item in ready]
            heapq.heapify(heap)
            queue_length = len(ready)

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


def MFQ_scheduler(processes,
                  first_queue,
                  second_queue,
                  third_queue,
                  waiting_queue,
                  CPU,
                  time,
                  levels,
                  verbose=True):
    """Multilevel Feedback Queue algorithm"""
    if first_queue:
        process = find_lowest_arrival(first_queue)
        time = RR_for_MLQ(process,
                          processes,
                          first_queue,
                          second_queue,
                          third_queue,
                          waiting_queue,
                          CPU,
                          time,
                          levels[0])
    elif second_queue:
        process = find_lowest_arrival(second_queue)
        time = RR_for_MLQ(process,
                          processes,
                          first_queue,
                          second_queue,
                          third_queue,
                          waiting_queue,
                          CPU,
                          time,
                          levels[1])
    elif third_queue:
        process = find_lowest_arrival(third_queue)
        time = RR_for_MLQ(process,
                          processes,
                          first_queue,
                          second_queue,
                          third_queue,
                          waiting_queue,
                          CPU,
                          time,
                          levels[2])
    else:
        update_waiting_queue(first_queue,second_queue,third_queue, waiting_queue)
        
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

def update_waiting_queue(first_queue,
                         second_queue,
                         third_queue,
                         waiting_queue):                        
    """updates the wait queue"""
    holder = waiting_queue.copy()
    if waiting_queue:
        for process in holder:
            duty = process.get_duty()
            duty[0] -= 1
            if duty[0] <= 0:
                duty.pop(0)
                process.set_status("running")
                process.set_duty(duty)
                if process.get_queue() == 0:
                    first_queue.append(process)
                elif process.get_queue() == 1:
                    second_queue.append(process)
                else:
                    third_queue.append(process)
                waiting_queue.remove(process)
            process.set_duty(duty)
    print(f"Before update: {len(waiting_queue)} waiting, {len(first_queue)} ready")

def RR_for_MLQ(process,
               processes,
               first_queue,
               second_queue,
               third_queue,
               waiting_queue,
               CPU,
               time,
               level):
    """customized Round Robin for MLQ"""
    response(process, time)
    process.set_wait_time(process.get_wait_time() + (time - process.get_arrival_time()))
    start_time = time
    
    print("just before the while loop")
    while level > 0 and process.get_duty()[0] > 0:
        level -= 1
        time += 1
        duty = process.get_duty()
        duty[0] -= 1
        process.set_duty(duty)
        add_ready(processes, first_queue, time)
        update_waiting_queue(first_queue,
                             second_queue,
                             third_queue,
                             waiting_queue)

    # quantum wasn't enough for process, so demote to lower queue
    if level == 0  and process.get_duty()[0] > 0:
        process.set_queue(process.get_queue() + 1)
        process.set_arrival_time(time)
        if process.get_queue()== 1:
            second_queue.append(process)
        else:
            third_queue.append(process)
        print(f"Process {process.get_ID()} moving to queue {process.get_queue()}")

    else: # process gave up cpu before quantum, so send it to waiting
        duty = process.get_duty()
        duty.pop(0)
        process.set_duty(duty)
        if len(duty) > 0:
            process.status = "waiting"
            waiting_queue.append(process)
        else:
            process.set_turnaround_time(process.get_wait_time() + (time - process.get_arrival_time()))

    CPU.append( dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=time,
                    Priority=process.get_priority()))
    return time
