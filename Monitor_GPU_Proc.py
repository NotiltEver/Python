import tkinter as tk
from tkinter import ttk
import psutil
import GPUtil
from time import sleep
import threading

# Function to get GPU usage information
def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append((gpu.name, gpu.load * 100, gpu.memoryUsed, gpu.memoryTotal))
    return gpu_info

# Function to get memory usage information
def get_memory_info():
    memory = psutil.virtual_memory()
    return memory.used / (1024 ** 3), memory.total / (1024 ** 3)

# Function to get CPU usage information
def get_cpu_info():
    return psutil.cpu_percent(interval=1)

# Function to update the GUI with the latest performance data
def update_performance():
    memory_used, memory_total = get_memory_info()
    memory_label.config(text=f"Memory Usage: {memory_used:.2f} GB / {memory_total:.2f} GB")
    
    gpu_info = get_gpu_info()
    for i, (name, load, mem_used, mem_total) in enumerate(gpu_info):
        gpu_labels[i].config(text=f"GPU {i+1} ({name}): Load: {load:.2f}%, Memory: {mem_used:.2f} MB / {mem_total:.2f} MB")

    cpu_usage = get_cpu_info()
    cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")

    root.after(1000, update_performance)

# Initialize the GUI
root = tk.Tk()
root.title("System Performance Monitor")

# CPU usage label
cpu_label = ttk.Label(root, text="CPU Usage: Calculating...", font=('Helvetica', 14))
cpu_label.pack(pady=10)

# Memory usage label
memory_label = ttk.Label(root, text="Memory Usage: Calculating...", font=('Helvetica', 14))
memory_label.pack(pady=10)

# GPU usage labels
gpu_labels = []
gpus = GPUtil.getGPUs()
for i, gpu in enumerate(gpus):
    label = ttk.Label(root, text=f"GPU {i+1} ({gpu.name}): Calculating...", font=('Helvetica', 14))
    label.pack(pady=5)
    gpu_labels.append(label)

# Start the update loop
update_performance()

# Run the GUI
root.mainloop()

