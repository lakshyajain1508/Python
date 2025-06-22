# Class & Object

Python is an object-oriented programming language, which means it allows the definition of **classes** and creation of **objects**. These are the fundamental building blocks of OOP (Object-Oriented Programming).

---

## What is a Class?

A **class** is like a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
```

---

## What is an Object?

An **object** is an instance of a class. When a class is defined, no memory or storage is allocated. Objects are created using the class.

```python
dog1 = Dog("Tommy", "Labrador")
dog2 = Dog("Bruno", "Pug")

dog1.bark()  # Output: Tommy says Woof!
dog2.bark()  # Output: Bruno says Woof!
```

---

## `__init__` Method

- A special method in Python classes.
- Called automatically when a new object is created.
- Used to initialize the object’s attributes.

```python
def __init__(self, name):
    self.name = name
```

---

## Why Use Classes and Objects?

- Code **reuse** via inheritance.
- Organize code with **encapsulation**.
- **Modular** and **scalable** programs.

---

## Real-Life Example

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Innova")
car2 = Car("Hyundai", "Creta")

car1.details()
car2.details()
```

---

## Summary

| Term   | Meaning |
|--------|---------|
| Class  | Blueprint for objects |
| Object | Instance of a class |
| Method | Function defined inside a class |
| Attribute | Variable associated with an object |

---
