# Functions

## Table of Contents

1. Introduction to Functions
2. Defining a Function
   - Function Syntax
   - Calling a Function
3. Function Arguments
   - Positional Arguments
   - Keyword Arguments
   - Default Arguments
   - Variable-length Arguments (*args and **kwargs)
4. Return Statement
5. Scope of Variables
   - Local Scope
   - Global Scope
   - Nonlocal Scope
6. Lambda Functions
7. Built-in Functions
8. Recursion
9. Practical Examples

---

## 1. Introduction to Functions

Functions are reusable blocks of code that perform a specific task. They help organize code into manageable sections, making it easier to read, debug, and maintain.

### Why Functions are Important

Functions promote code reusability and modularity. By breaking down complex problems into smaller, manageable functions, you can create more efficient and maintainable code.

---

## 2. Defining a Function

A function is defined using the `def` keyword, followed by the function name and parentheses. The function body contains the code to be executed.

### Function Syntax

```python
def function_name(parameters):
    # block of code
    return value
```

### Example

```python
# Defining a simple function
def greet():
    print("Hello, Lakshya!")

# Calling the function
greet()
```

### Calling a Function

To execute a function, you call it by its name followed by parentheses.

```python
# Calling the greet function
greet()
```

---

## 3. Function Arguments

Functions can accept arguments (also known as parameters) to provide input data.

### Positional Arguments

Positional arguments are the most common type of arguments. They are passed to the function in the order they are defined.

```python
# Function with positional arguments
def add(a, b):
    return a + b

# Calling the function with arguments
result = add(5, 3)
print(result)  # Output: 8
```

### Keyword Arguments

Keyword arguments are passed to the function by explicitly naming each parameter along with its value.

```python
# Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Calling the function with keyword arguments
introduce(name="Lakshya", age=18)
```

### Default Arguments

Default arguments are parameters that assume a default value if no argument is provided during the function call.

```python
# Function with default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without an argument
greet()  # Output: Hello, Guest!

# Calling the function with an argument
greet("Lakshya")  # Output: Hello, Lakshya!
```

### Variable-length Arguments (*args and **kwargs)

Variable-length arguments allow you to pass an arbitrary number of arguments to a function.

#### *args

`*args` allows a function to accept any number of positional arguments.

```python
# Function with *args
def sum_all(*args):
    return sum(args)

# Calling the function with multiple arguments
result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

#### **kwargs

`**kwargs` allows a function to accept any number of keyword arguments.

```python
# Function with **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with multiple keyword arguments
print_info(name="Lakshya", age=18, city="Mumbai")
```

---

## 4. Return Statement

The `return` statement is used to exit a function and return a value to the caller.

### Example

```python
# Function with return statement
def multiply(a, b):
    return a * b

# Calling the function and storing the result
result = multiply(5, 3)
print(result)  # Output: 15
```

---

## 5. Scope of Variables

The scope of a variable determines where it can be accessed in the code. Python has three types of scopes: local, global, and nonlocal.

### Local Scope

Variables defined inside a function are in the local scope and can only be accessed within that function.

```python
# Local scope example
def greet():
    message = "Hello, world!"  # Local variable
    print(message)

greet()
# print(message)  # This will cause an error as 'message' is not accessible outside the function
```

### Global Scope

Variables defined outside any function are in the global scope and can be accessed from anywhere in the code.

```python
# Global scope example
message = "Hello, world!"  # Global variable

def greet():
    print(message)

greet()  # Output: Hello, world!
print(message)  # Output: Hello, world!
```

### Nonlocal Scope

The `nonlocal` keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

```python
# Nonlocal scope example
def outer():
    message = "Hello, world!"  # Enclosing variable

    def inner():
        nonlocal message
        message = "Hello, Lakshya!"

    inner()
    print(message)

outer()  # Output: Hello, Lakshya!
```

---

## 6. Lambda Functions

Lambda functions are small anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
# Lambda function example
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

### Usage in Higher-order Functions

Lambda functions are often used in higher-order functions like `map()`, `filter()`, and `reduce()`.

```python
# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

## 7. Built-in Functions

Python provides several built-in functions that you can use directly without defining them. Some common built-in functions include `len()`, `max()`, `min()`, `sum()`, `sorted()`, and `abs()`.

### Examples

```python
# Using built-in functions
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # Output: 5
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1
print(sum(numbers))  # Output: 15
print(sorted(numbers, reverse=True))  # Output: [5, 4, 3, 2, 1]
print(abs(-10))  # Output: 10
```

---

## 8. Recursion

Recursion is a technique where a function calls itself to solve a problem. It is useful for tasks that can be broken down into similar sub-tasks.

### Example: Factorial Calculation

```python
# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Example: Fibonacci Sequence

```python
# Recursive function to generate Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
```

---

## 9. Practical Examples

### Example 1: Temperature Conversion

```python
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))  # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
```

### Example 2: Prime Number Check

```python
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
```

### Example 3: Palindrome Check

```python
# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

---