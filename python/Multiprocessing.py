"""Multiprocessing in Python allows you to run multiple processes concurrently, 
taking advantage of multiple CPU cores. Each process runs independently,
 has its own memory space, and can execute its tasks concurrently.
   This is useful for CPU-bound tasks where parallelism can significantly improve performance.

"""

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))




        import multiprocessing

# Function to calculate the square of a number
def calculate_square(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a list to hold process objects
    processes = []

    # Create a process for each number
    for number in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(number,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
