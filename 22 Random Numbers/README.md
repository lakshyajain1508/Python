# Random Number Generator

A simple Python script that generates a user-specified number of random integers within a set range.

## Features

-   **User Input:** Prompts the user to specify how many random numbers to generate.
-   **Error Handling:** Catches non-integer input to prevent crashes.
-   **Defined Range:** Generates random numbers between 1 and 70 (inclusive).

## Getting Started

### Prerequisites

You only need **Python 3** installed on your system to run this script.

### How to Run

1.  Save the Python code (from the previous responses) into a file named `random_numbers.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the following command:

    ```bash
    python random_numbers.py
    ```

5.  Follow the on-screen instructions and enter the number of random numbers you wish to generate.

## Code Overview

The script uses Python's built-in `random` module.

```python
import random

# A loop to handle incorrect user input
while True:
    try:
        num_to_generate = int(input("How many random numbers (1-100) would you like to generate? "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# A loop to generate the numbers
print(f"\nGenerating {num_to_generate} random numbers between 1 and 70:")
for i in range(num_to_generate):
    print(random.randint(1, 100))
```