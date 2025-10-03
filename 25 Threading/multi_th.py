from threading import Thread
import time

def task1():
    print("Task 1 started by Thread 1.")
    time.sleep(5)
    print("Task 1 completed by Thread 1.")

def task2():
    print("\nTask 2 started by Thread 2.")
    time.sleep(10)
    print("Task 2 completed by Thread 2.")

def main_threaded():
    print("Multi-threaded program started.")
    
    # 1. Create Thread objects, targeting the functions
    thread1 = Thread(target=task1)
    thread2 = Thread(target=task2)
    
    # 2. Start the threads (tasks begin executing concurrently)
    thread1.start()
    thread2.start()
    
    # 3. Wait for both threads to complete before moving on
    # (This is crucial to ensure the main program waits for the concurrent tasks)
    thread1.join()
    thread2.join()
    
    print("Multi-threaded program completed.")

if __name__ == "__main__":
    main_threaded()