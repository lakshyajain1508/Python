# Python Data Types

Python has a wide variety of built-in data types that help store and manipulate different kinds of data efficiently. These data types are categorized into **basic**, **collection**, **binary**, and **special types**.

---

## 🔹 Basic Data Types

| Type     | Description                  | Example                         |
|----------|------------------------------|---------------------------------|
| `int`    | Integer numbers              | `x = 42`                        |
| `float`  | Decimal numbers              | `pi = 3.14`                     |
| `complex`| Complex numbers              | `z = 2 + 3j`                    |
| `bool`   | Boolean values               | `is_valid = True`              |
| `str`    | Text (string of characters)  | `name = "Python"`              |
| `None`   | Null / No value              | `result = None`                |

---

## 🔹 Collection Data Types

| Type      | Description                        | Example                                   |
|-----------|------------------------------------|-------------------------------------------|
| `list`    | Ordered, mutable collection        | `fruits = ["apple", "banana", "cherry"]` |
| `tuple`   | Ordered, immutable collection      | `point = (10, 20)`                        |
| `range`   | Immutable sequence of numbers      | `r = range(1, 5)`                         |
| `set`     | Unordered collection of unique items| `colors = {"red", "green"}`              |
| `frozenset`| Immutable version of set          | `fs = frozenset(["a", "b", "c"])`         |
| `dict`    | Key-value mapping                  | `person = {"name": "Alice", "age": 25}`  |

---

## 🔹 Binary Data Types

| Type       | Description                 | Example                                    |
|------------|-----------------------------|--------------------------------------------|
| `bytes`    | Immutable binary data       | `b = b"hello"`                             |
| `bytearray`| Mutable binary data         | `ba = bytearray([65, 66, 67])`             |
| `memoryview`| Memory-efficient view of bytes| `mv = memoryview(b"data")`              |

---

## 🔹 Type Checking

You can check the type of a variable using the `type()` function:

```python
x = 10
print(type(x))         # <class 'int'>

s = "hello"
print(type(s))         # <class 'str'>
