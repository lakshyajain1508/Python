# Random Number Generator & OTP Generator
---
## Random Number
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
--- 

## OTP Generator

This is a simple and clean Python script that generates a one-time password (OTP) of a user-specified length. It's a great example of how to handle user input and generate random, non-sensitive data in Python.

## Features

* **Customizable Length:** The user can specify the exact length of the OTP they want to generate.

* **Default Value:** If the user doesn't enter a length, the script defaults to generating a 4-digit OTP.

* **No Duplicates:** The `random.choice()` function ensures each digit is randomly selected and can appear more than once, which is a standard requirement for OTPs.

## How to Run the Script

1. Make sure you have **Python 3** installed on your system.

2. Save the code into a file named `otp_generator.py`.

3. Open a terminal or command prompt.

4. Navigate to the directory where you saved the file.

5. Run the script using the following command:
   
6. Follow the on-screen prompt to enter the desired length for your OTP. Press Enter to use the default length of 4.

## Code Breakdown

### 1. Import Statements
* `import random`: This line imports the `random` module, which is a built-in Python library for generating random numbers and making random choices. It is crucial for picking the digits of the OTP.

* `import string`: This line imports the `string` module. The code uses `string.digits` to easily access a string containing all the digit characters from `'0'` to `'9'`. This is more readable and less error-prone than typing the string manually.

### 2. The `generate_otp` Function
* `def generate_otp(length=4):`: This defines a function named `generate_otp` that takes one argument, `length`. The `=4` makes this a **default parameter**. If the function is called without a `length` argument, it will use the value 4.

* `characters = string.digits`: This assigns the string `'0123456789'` (from the `string` module) to the `characters` variable.

* `otp = ''.join(random.choice(characters) for _ in range(length))`: This is the core logic. It uses a **generator expression** to efficiently build the OTP.

  * `random.choice(characters)`: Selects a single, random digit from the `characters` string.

  * `for _ in range(length)`: This repeats the random selection process `length` number of times. The underscore `_` is a convention for a variable you don't need to use.

  * `''.join(...)`: This method takes all the randomly selected digits and joins them together into a single string. The empty string `''` at the beginning means there will be no separator between the digits.

* `return otp`: This line sends the final generated OTP string back to the part of the code that called the function.

### 3. User Input and Execution
* `num = int(input(...) or 4)`: This line prompts the user for input and handles the conversion to an integer. The `or 4` part is a Python trick that assigns the default value `4` if the user just presses Enter without typing anything.

* `if __name__ == "__main__":`: This is a standard Python pattern that ensures the code inside this block only runs when the script is executed directly (as opposed to when it is imported as a module into another script).

* `otp_code_1 = generate_otp(length=num)`: This calls the `generate_otp` function, passing the user-specified length (`num`) as the argument. The returned OTP is stored in the `otp_code_1` variable.

* `print(...)`: Finally, this line prints the generated OTP to the console using an **f-string** for clean formatting.