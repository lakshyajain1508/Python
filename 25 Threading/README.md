# Threading in Python

This repository demonstrates the fundamental difference between **single-threaded (sequential)** and **multi-threaded (concurrent)** program execution in Python using the `time.sleep()` function to simulate time-consuming tasks.

---

## 1. Single-Threaded (Sequential) Execution

In a single-threaded program, tasks are executed one after the other. A new task can only start once the previous one has completely finished. This is the simplest and default mode of execution.

### 💻 Code (`single_threaded.py`)

The provided code runs `task1` and then `task2` sequentially.

```python
import time

def task1():
    print("Task 1 started.")
    time.sleep(5)  # Simulate a 5-second operation
    print("Task 1 completed.")

def task2():
    print("Task 2 started.")
    time.sleep(10) # Simulate a 10-second operation
    print("Task 2 completed.")

def main():
    print("Single-threaded program started.")
    task1()
    task2()
    print("Single-threaded program completed.")

if __name__ == "__main__":
    main()
````

### ⏱️ Execution Time

The total time taken will be the **sum** of the time for all tasks:

  * **Total Time** $\approx$ (Time for `task1`) $+$ (Time for `task2`)
  * **Total Time** $\approx 5$ seconds $+ 10$ seconds $= \mathbf{15\ seconds}$

### 💡 Key Takeaway

The program is **blocked** on `time.sleep(5)` before it can even begin executing `task2`.

-----

## 2\. Multi-Threaded (Concurrent) Execution

Multithreading allows a program to handle multiple tasks seemingly at the same time (concurrently). The operating system rapidly switches between the threads, allowing both tasks to make progress independently. This is ideal for **I/O-bound** tasks (like waiting for network requests or file reads).

```python
from threading import Thread
import time

def task1():
    print("Task 1 started by Thread 1.")
    time.sleep(5)
    print("Task 1 completed by Thread 1.")

def task2():
    print("Task 2 started by Thread 2.")
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
```

### ⏱️ Execution Time

Since the tasks run concurrently, the total time taken will be roughly the duration of the **longest** task:

  * **Total Time** $\approx$ $\mathbf{10\ seconds}$ (The time taken by the longer task, `task2`).

### 💡 Key Takeaway

The program doesn't have to wait for `task1` to finish before starting `task2`. They run in parallel, dramatically reducing the overall execution time for this kind of simulation.

-----

## 🚀 Applications of Multithreading

Multithreading is a powerful concept used in various real-world scenarios, primarily to improve **responsiveness** and **throughput**.

| Application Area | Use Case | Benefit |
| :--- | :--- | :--- |
| **User Interfaces (GUI)** | Keeping the UI responsive while performing a long calculation or data fetch in the background. | Prevents the application from freezing; better user experience. |
| **Web Servers** | Handling multiple client requests simultaneously (e.g., serving 100 users at once). | High throughput and efficient resource utilization. |
| **Networking** | Downloading multiple files concurrently or having one thread listening for new connections while another processes data. | Significantly faster I/O operations. |
| **Games** | Handling background tasks like loading assets, updating physics, or checking for user input without impacting the main rendering loop. | Smoother and more complex game environments. |

### ⚠️ A Note on Python and the GIL

It's important to mention the **Global Interpreter Lock (GIL)** in CPython. The GIL ensures that only one thread can execute Python **bytecode** at a time. This means multithreading in Python is excellent for **I/O-bound** tasks (where the thread spends most of its time waiting, releasing the GIL), but it does **not** provide true parallel execution for **CPU-bound** tasks (like heavy calculations). For true CPU parallelism, Python programmers typically use the `multiprocessing` module.
