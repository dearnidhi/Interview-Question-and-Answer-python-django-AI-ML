"""Threading in Python refers to the ability of a program to execute multiple threads (smaller units of a program) concurrently.
 A thread is a lightweight, independent unit of execution that runs within a process.
   Threading allows a program to perform multiple tasks simultaneously, 
   making it more responsive and efficient.

"""


import threading
import time
def print_numbers():
    for i in range(6):
        time.sleep(2)
        print(i)

def print_latter():
    for latter in 'ABCD':
        time.sleep(4)
        print(latter)

thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_latter)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Both thread has been finished")


#Share data between threads
"""In Python, when you're dealing with multiple threads, 
sharing data between threads needs to be done carefully 
to avoid race conditions and data corruption. 
The threading module in Python provides tools for
synchronization to help manage shared resources.
"""
import threading

# Shared data
shared_data = 0

# Lock for synchronization
lock = threading.Lock()

def increment_shared_data():
    global shared_data
    for _ in range(1000000):
        with lock:
            shared_data += 1

def decrement_shared_data():
    global shared_data
    for _ in range(1000000):
        with lock:
            shared_data -= 1

# Create two threads
thread1 = threading.Thread(target=increment_shared_data)
thread2 = threading.Thread(target=decrement_shared_data)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Final shared data:", shared_data)
