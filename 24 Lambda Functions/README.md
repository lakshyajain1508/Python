# Python Lambda Functions

This repository/guide provides examples and explanations for using **Lambda Functions** in Python, ranging from basic syntax to advanced applications with built-in functions and closures.

---

## What is a Lambda Function?

A lambda function is a small, **anonymous** (meaning it has no name) function defined in a single line using the `lambda` keyword. It can take any number of arguments, but can only have **one expression**.

### 💡 Core Syntax
```python
lambda arguments: expression
```
### 1. Beginner: Basic Syntax and Execution
Lambda functions are simple to define and are typically used for quick, simple operations.

**Example 1: Basic Addition**
Assign the lambda function to a variable and call it like a regular function.
```python
# A lambda function that adds two numbers (a and b)
add = lambda a, b: a + b

# Execution
result = add(10, 5) 
print(result)  # Output: 15
```
### Example 2: Squaring a Number
```python
square = lambda x: x * x

# Execution
result = square(9)
print(result)  # Output: 81
```

### 2. Intermediate: Functional Programming Tools
Lambda functions truly shine when used as key functions or predicate functions with Python's higher-order functions: map(), filter(), and sorted().

`map()`: Transforming Elements
Applies the lambda function to every item in an iterable.

```Python

numbers = [1, 2, 3, 4, 5]

# Use map to double every number
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Output: [2, 4, 6, 8, 10]
print(doubled_numbers)
```
`filter()`: Selecting Elements
Uses the lambda function as a test to select elements that evaluate to True.
```Python

scores = [75, 90, 45, 88, 62]

# Use filter to select scores greater than 80
high_scores = list(filter(lambda s: s > 80, scores))

# Output: [90, 88]
print(high_scores)
```
`sorted()`: Custom Sorting
Uses the lambda function in the key argument to define the sorting criteria.
```Python

data = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Sort the list of tuples based on the second element (the score)
sorted_by_score = sorted(data, key=lambda item: item[1])

# Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
print(sorted_by_score)
```
### 3. Advanced: Conditional Logic and Closures
Conditional Logic (Ternary Operator)
Since a lambda must be a single expression, conditional logic is achieved using the ternary operator: value_if_true if condition else value_if_false.
```Python

# Check if a number is positive or negative
check_sign = lambda x: "Positive" if x >= 0 else "Negative"

print(check_sign(10))  # Output: Positive
print(check_sign(-5))  # Output: Negative
```
### Function Closures (Factory Functions)
A lambda can be returned from another function, creating a closure that "remembers" the value of a variable from its outer scope.

```Python

def make_power_function(exponent):
    # The lambda function "captures" the 'exponent' variable
    return lambda base: base ** exponent

# Create a 'square' function (power of 2)
square_func = make_power_function(2) 
print(square_func(5))  # Output: 25 (5^2)

# Create a 'cube' function (power of 3)
cube_func = make_power_function(3)
print(cube_func(2))    # Output: 8 (2^3)
```

## 🛑 Limitations of Lambda Functions
1. **Single Expression Only:** Cannot contain multiple statements (e.g., loops, multiple assignment lines, `if`/`elif`/`else blocks`).

2. **No Docstrings:** Cannot have documentation strings (`"""Docstring"""`).

3. **Readability:** Overly complex lambdas become difficult to read and should be replaced with a standard `def` function.