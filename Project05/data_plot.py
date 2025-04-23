"""
    Name: Desmond Frimpong
    Course: CS337
    Project: 5
    Date: 04/07/2025
    File: data_plot.py

    This script is used to plot the performance of the serial code
    against the performance of the multitasking code.
"""
import matplotlib.pyplot as plt
from serial_code import main as serial_main
from multitasking_code import main as multitask_main

def plot_performance(serial_times, multitask_times):
    """
        Plot the performance of serial vs multitasking code.
        :param serial_times: List of execution times for serial code.
        :param multitask_times: List of execution times for multitasking code.
    """
    # files = list(serial_times.keys())
    # serial_values = [serial_times[file] for file in files]
    # multitask_values = [multitask_times[file] for file in files]
    files = [i for i in range(len(serial_times))]

    plt.figure(figsize=(12, 6))
    
    # Plot both lines
    plt.plot(files, serial_times, marker='o', label='Serial', linewidth=2)
    plt.plot(files, multitask_times, marker='s', label='Multitask', linewidth=2)

    # Formatting
    plt.xlabel('Reddit Comment Files')
    plt.ylabel('Processing Time (seconds)')
    plt.title('Serial vs Multitasking Total File Processing Time')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    multitask, serial = [], []
    for i in range(10):
        serial_performance, serial_duration = serial_main()
        multitask_performance, multitask_duration = multitask_main()
        serial.append(serial_duration)
        multitask.append(multitask_duration)
    plot_performance(serial, multitask)

    # Get performance data from both serial and multitasking code
    # with open("performance_data.txt", "w") as file:
    #     file.write("Run, Serial Time (s), Multitask Time (s)\n")
    #     for i in range(10):
    #         serial_performance, serial_duration = serial_main()
    #         multitask_performance, multitask_duration = multitask_main()
    #         file.write(f'{i+1}, {serial_duration:.3f}, {multitask_duration:.3f}\n')

    # serial_performance, _ = serial_main()
    # multitask_performance, _ = multitask_main()

    # Plot the performance comparison
    #plot_performance(serial_performance, multitask_performance)