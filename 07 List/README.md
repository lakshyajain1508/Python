# List

## Table of Contents

1. Introduction to Lists
2. Creating Lists
3. Accessing List Elements
   - Indexing
   - Negative Indexing
   - Slicing
4. Modifying Lists
   - Changing Elements
   - Adding Elements
   - Removing Elements
5. List Operations
   - Concatenation
   - Repetition
   - Membership
   - Iteration
6. List Methods
   - append()
   - extend()
   - insert()
   - remove()
   - pop()
   - clear()
   - index()
   - count()
   - sort()
   - reverse()
   - copy()
7. List Comprehensions
8. Nested Lists
9. Practical Examples

---

## 1. Introduction to Lists

Lists are one of the most versatile and commonly used data structures in Python. They are ordered collections of items, which can be of different types, including integers, strings, and even other lists.

### Why Lists are Important

Lists are essential for storing, organizing, and manipulating collections of data. They provide a wide range of functionalities that make it easy to perform various operations on data.

---

## 2. Creating Lists

A list is created by placing all the items (elements) inside square brackets `[]`, separated by commas.

### Syntax

```python
list_name = [item1, item2, item3, ...]
```

### Examples

```python
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a mixed list
mixed_list = [1, "apple", 3.5, True]
```

---

## 3. Accessing List Elements

You can access elements of a list using indexing and slicing.

### Indexing

Indexing allows you to access individual elements in a list. The index starts from 0.

```python
# Accessing elements by index
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

### Negative Indexing

Negative indexing allows you to access elements from the end of the list. The index `-1` refers to the last item.

```python
# Accessing elements using negative indexing
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
```

### Slicing

Slicing allows you to access a range of elements in a list. The syntax is `list[start:end]`, where `start` is the starting index and `end` is the ending index (exclusive).

```python
# Accessing a range of elements using slicing
print(fruits[0:2])  # Output: ['apple', 'banana']
print(fruits[1:])   # Output: ['banana', 'cherry']
print(fruits[:2])   # Output: ['apple', 'banana']
```

---

## 4. Modifying Lists

You can modify lists by changing, adding, or removing elements.

### Changing Elements

You can change the value of a specific element by accessing its index.

```python
# Changing elements in a list
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

### Adding Elements

#### append()

The `append()` method adds an element to the end of the list.

```python
# Adding elements using append()
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
```

#### insert()

The `insert()` method adds an element at a specified position.

```python
# Adding elements using insert()
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'orange']
```

### Removing Elements

#### remove()

The `remove()` method removes the first occurrence of a specified value.

```python
# Removing elements using remove()
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
```

#### pop()

The `pop()` method removes the element at a specified position and returns it. If no index is specified, it removes the last item.

```python
# Removing elements using pop()
last_fruit = fruits.pop()
print(last_fruit)  # Output: orange
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

#### clear()

The `clear()` method removes all elements from the list.

```python
# Clearing the list
fruits.clear()
print(fruits)  # Output: []
```

---

## 5. List Operations

### Concatenation

You can concatenate lists using the `+` operator.

```python
# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
```

### Repetition

You can repeat lists using the `*` operator.

```python
# Repeating lists
list1 = [1, 2, 3]
result = list1 * 2
print(result)  # Output: [1, 2, 3, 1, 2, 3]
```

### Membership

You can check if an element is in a list using the `in` keyword.

```python
# Checking membership
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("orange" in fruits)  # Output: False
```

### Iteration

You can iterate over the elements of a list using a `for` loop.

```python
# Iterating over a list
for fruit in fruits:
    print(fruit)
```

---

## 6. List Methods

Python provides several built-in methods for performing operations on lists.

### append()

Adds an element to the end of the list.

```python
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

### extend()

Extends the list by appending all the elements from another list.

```python
fruits.extend(["mango", "grape"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'mango', 'grape']
```

### insert()

Inserts an element at a specified position.

```python
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'mango', 'grape']
```

### remove()

Removes the first occurrence of a specified value.

```python
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'mango', 'grape']
```

### pop()

Removes the element at a specified position and returns it.

```python
last_fruit = fruits.pop()
print(last_fruit)  # Output: grape
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'mango']
```

### clear()

Removes all elements from the list.

```python
fruits.clear()
print(fruits)  # Output: []
```

### index()

Returns the index of the first occurrence of a specified value.

```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1
```

### count()

Returns the number of times a specified value occurs in the list.

```python
count = fruits.count("apple")
print(count)  # Output: 1
```

### sort()

Sorts the list in ascending order by default.

```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]
```

### reverse()

Reverses the order of the list.

```python
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]
```

### copy()

Returns a shallow copy of the list.

```python
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']
```

---

## 7. List Comprehensions

List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause.

### Syntax

```python
[expression for item in iterable if condition]
```

### Examples

```python
# Creating a list of squares
squares = [x ** 2 for x in range(10)]
print(squares) 

 # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## 8. Nested Lists

Nested lists are lists within lists. They allow you to create complex data structures.

### Example

```python
# Creating a nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(nested_list[0])       # Output: [1, 2, 3]
print(nested_list[0][1])    # Output: 2

# Iterating through a nested list
for sublist in nested_list:
    for item in sublist:
        print(item, end=' ')  # Output: 1 2 3 4 5 6 7 8 9
```

---

## 9. Practical Examples

### Example 1: Removing Duplicates

```python
# Function to remove duplicates from a list
def remove_duplicates(input_list):
    return list(set(input_list))

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]
```

### Example 2: Flattening a Nested List

```python
# Function to flatten a nested list
def flatten(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = flatten(nested_list)
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 3: List Comprehension with Condition

```python
# Using list comprehension to filter a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(squared_evens)  # Output: [4, 16, 36, 64, 100]
```

---

