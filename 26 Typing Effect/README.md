# 🎵 Python Typing Effect

This simple Python script uses the `time` module to simulate a "human typing" effect for displaying text, line by character by character, often used for displaying lyrics or dialogue in a more engaging way.

The provided example displays a snippet of the song 

<a href="https://github.com/lakshyajain1508/Python/blob/main/26%20Typing%20Effect/typing.py"><span>**"Arz Kiya Hai Lyrics"**.<span></a>

<a href="https://github.com/lakshyajain1508/Python/blob/main/26%20Typing%20Effect/lyrics.py"><span>**"Agar Tum Saath Ho lyrics"**.<span></a>

---

### 🚀 How It Works

The core of the effect lies in the `type_lyrics` function, which leverages three key Python concepts:

1.  **Iteration:** A `for` loop iterates through every **character** in the line string.
2.  **`time.sleep()`:** The `time.sleep(typing_speed)` call pauses the execution for a short duration (default is $0.065$ seconds) after each character is printed.
3.  **Standard Output Control:**
    * `print(char, end='', ...)` ensures that the next character is printed **on the same line** immediately after the previous one (instead of starting a new line).
    * `flush=True` forces the output buffer to be written to the console instantly, which is necessary for the smooth, character-by-character display.

## ⚙️ Requirements

This script uses only built-in Python modules and requires no external libraries.

* **Python 3.x**

## 💡 Customization

You can easily modify the script to display any text you like:

1.  **Change the Lyrics:** Update the list in the `lyrics` variable inside the `print_lyrics` function.
2.  **Adjust Speeds:**
    * **Typing Speed:** Modify the `typing_speed` parameter in the `type_lyrics` function (smaller number = faster typing).
    * **Line Delays:** Update the list of floats in the `delays` variable to control the pause time *between* lines.
3. The `import time` statement brings in Python's built-in **`time` module**, which provides a set of functions for working with time, including measuring elapsed time, managing delays, and representing dates.



#### Key Function: `time.sleep()`

The most critical function for your script is **`time.sleep(secs)`**.

* **Purpose:** It halts the execution of the current thread for a specified number of seconds.
* **Mechanism in Your Script:**
    * In `type_lyrics`, `time.sleep(typing_speed)` pauses the script for $0.065$ seconds after printing *each* character. This is what creates the **typing animation effect**.
    * In `print_lyrics`, it's used to create **delays between lines** and an initial pause before the lyrics start.

***

#### Other Useful Functions in the `time` Module

While your script only uses `sleep()`, the `time` module is extensive and useful for other tasks:

| Function | Purpose | Example Use Case |
| :--- | :--- | :--- |
| **`time.time()`** | Returns the current system time as a floating-point number, representing the seconds elapsed since the **Epoch** (January 1, 1970, 00:00:00 UTC). | Measuring the **execution time** of a block of code (benchmarking). |
| **`time.ctime([secs])`** | Converts a time expressed in seconds since the Epoch (like that returned by `time.time()`) to a readable string format (e.g., `'Wed Oct 15 17:40:34 2025'`). | Logging and displaying the current time in a user-friendly way. |
| **`time.perf_counter()`** | Returns a high-resolution time measurement with the primary purpose of measuring **short durations** or code performance. | Accurate micro-benchmarking of functions or algorithms. |
| **`time.struct_time`** | A named tuple structure used to represent time as a set of nine attributes (year, month, day, hour, minute, second, weekday, day of year, DST flag). | Used by functions like `time.gmtime()` and `time.localtime()` to provide detailed time information. |

***

#### The Concept of the Epoch

A fundamental concept in the `time` module is the **Epoch**.

* The floating-point number returned by `time.time()` is the total number of seconds that have passed since this moment.
