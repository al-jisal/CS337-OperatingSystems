"""
Name: Desmond Frimpong
Course: CS337
Project: 2
Date: 02/26/2025
File: process.py
This file is a structure that holds process information
"""
class Process:
    """A process object"""
    def __init__(self, id, duty, arrival_time, priority):
        """Constructor for Process class"""
        self.id = id
        self.duty = duty
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = None
        self.status = "running"
        self.queue = 0

    def __repr__(self):
        return f"Process(id:{self.id})"
    
    def get_ID(self):
        """returns the ID of a process"""
        return self.id
    
    def get_queue(self):
        """
        returns the queue number that a process resides
        in a multilevel feedback queue
        """
        return self.queue

    def set_queue(self, queue):
        """sets the queue number of a process"""
        self.queue = queue

    def get_status(self):
        """returns the status of a process"""
        return self.status
    
    def set_status(self, status):
        """sets the status of a process"""
        self.status = status

    def get_response_time(self):
        """returns the response time of a process"""
        return self.response_time

    def set_response_time(self, response_time):
        """sets the response time of a process"""
        self.response_time = response_time

    def get_duty(self):
        """returns the burst time of a process"""
        return self.duty
    
    def set_duty(self, duty):
        """sets the burst time of a process"""
        self.duty = duty

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
