"""
This file is a structure that holds process information
"""
class Process:
    """A process object"""
    def __init__(self, id, burst_time, arrival_time, priority):
        """Constructor for Process class"""
        self.id = id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0
    
    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def get_ID(self):
        """returns the ID of a process"""
        return self.id
    
    def get_burst_time(self):
        """returns the burst time of a process"""
        return self.burst_time
    
    def set_burst_time(self, burst_time):
        """sets the burst time of a process"""
        self.burst_time = burst_time

    def get_arrival_time(self):
        """returns the arrival time of a process"""
        return self.arrival_time
    
    def set_arrival_time(self, arrival_time):
        """sets the arrival time of a process"""
        self.arrival_time = arrival_time

    def get_priority(self):
        """returns the priority of a process"""
        return self.priority
    
    def set_priority(self, priority):
        """sets the priority of a process"""
        self.priority = priority

    def get_wait_time(self):
        """returns the wait time of a process"""
        return self.wait_time
    
    def set_wait_time(self, wait_time):
        """sets the wait time of a process"""
        self.wait_time = wait_time

    def get_turnaround_time(self):
        """returns the turn around time of a process"""
        return self.turnaround_time
    
    def set_turnaround_time(self, turnaround_time):
        """sets the turn around time of a process"""
        self.turnaround_time = turnaround_time
