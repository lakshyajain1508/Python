# Inheritance

### **1. Introduction to Python Inheritance**

Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP) in Python. It allows you to create a new class (child class) that inherits attributes and methods from an existing class (parent class). This promotes code reusability and helps to maintain a clean and organized codebase.

In this tutorial, we'll explore the concept of inheritance in detail, understand different types of inheritance, learn about method overriding, and see how the `super()` function is used in inheritance. We'll also look at practical examples and best practices for implementing inheritance in Python.

---

### **2. Understanding the Basics of Inheritance**

#### **What is Inheritance?**

Inheritance in Python is a mechanism that allows one class to inherit attributes and methods from another class. The class that inherits is called the child class or subclass, and the class from which it inherits is called the parent class or superclass.

**Example:**
```python
class Parent:
    def parent_method(self):
        print("This is a parent class method.")

class Child(Parent):
    pass

# Creating an object of the Child class
child_obj = Child()
child_obj.parent_method()
```

**Explanation:**
- In this example, the `Child` class inherits the `parent_method()` from the `Parent` class.

#### **Benefits of Inheritance**

- **Code Reusability:** You can reuse the code from the parent class in the child class.
- **Simplifies Code Maintenance:** Changes made in the parent class are automatically reflected in the child class.
- **Extensibility:** You can add new features to a child class without modifying the parent class.

#### **Terminology: Parent and Child Classes**

- **Parent Class (Superclass):** The class whose properties and methods are inherited by another class.
- **Child Class (Subclass):** The class that inherits properties and methods from the parent class.

---

### **3. Creating a Simple Inheritance Example**

Let's create a simple example to demonstrate inheritance.

**Example:**
```python
class Animal:
    def sound(self):
        print("This is an animal sound.")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Creating an object of the Dog class
dog = Dog()
dog.sound()  # Inherited from Animal class
dog.bark()   # Defined in Dog class
```

**Explanation:**
- The `Dog` class inherits the `sound()` method from the `Animal` class.
- Additionally, the `Dog` class defines its own method, `bark()`.

---

### **4. Types of Inheritance in Python**

Python supports different types of inheritance, allowing you to design complex class hierarchies. Let's explore the main types of inheritance.

#### **4.1 Single Inheritance**

In single inheritance, a child class inherits from one parent class.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        print("Child class method.")

child = Child()
child.method()  # Output: Child class method.
```

#### **4.2 Multiple Inheritance**

In multiple inheritance, a child class inherits from more than one parent class.

**Example:**
```python
class Parent1:
    def method1(self):
        print("Parent1 class method.")

class Parent2:
    def method2(self):
        print("Parent2 class method.")

class Child(Parent1, Parent2):
    pass

child = Child()
child.method1()  # Output: Parent1 class method.
child.method2()  # Output: Parent2 class method.
```

**Explanation:**
- The `Child` class inherits methods from both `Parent1` and `Parent2`.

#### **4.3 Multilevel Inheritance**

In multilevel inheritance, a child class inherits from a parent class, and another child class inherits from that child class.

**Example:**
```python
class Grandparent:
    def grandparent_method(self):
        print("Grandparent class method.")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent class method.")

class Child(Parent):
    pass

child = Child()
child.grandparent_method()  # Inherited from Grandparent class
child.parent_method()       # Inherited from Parent class
```

**Explanation:**
- The `Child` class inherits methods from both `Parent` and `Grandparent`.

#### **4.4 Hierarchical Inheritance**

In hierarchical inheritance, multiple child classes inherit from a single parent class.

**Example:**
```python
class Parent:
    def parent_method(self):
        print("Parent class method.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

child1 = Child1()
child2 = Child2()
child1.parent_method()  # Inherited from Parent class
child2.parent_method()  # Inherited from Parent class
```

#### **4.5 Hybrid Inheritance**

Hybrid inheritance is a combination of two or more types of inheritance.

**Example:**
```python
class Base:
    def base_method(self):
        print("Base class method.")

class Parent1(Base):
    pass

class Parent2(Base):
    pass

class Child(Parent1, Parent2):
    pass

child = Child()
child.base_method()  # Inherited from Base class
```

**Explanation:**
- The `Child` class inherits from `Parent1` and `Parent2`, both of which inherit from the `Base` class.

[Back to Top](#table-of-contents)

---

### **5. Method Overriding**

#### **Concept of Method Overriding**

Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. This allows the child class to modify or enhance the behavior of the inherited method.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        print("Child class method (overridden).")

child = Child()
child.method()  # Output: Child class method (overridden).
```

**Explanation:**
- The `Child` class overrides the `method()` from the `Parent` class, providing its own implementation.

[Back to Top](#table-of-contents)

---

### **6. Using `super()` Function**

The `super()` function in Python is used to call a method from the parent class in the child class. This is useful when you want to extend the functionality of a parent class method in the child class.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        super().method()  # Call the parent class method
        print("Child class method (extended).")

child = Child()
child.method()
```

**Output:**
```plaintext
Parent class method.
Child class method (extended).
```

**Explanation:**
- The `super().method()` calls the method from the parent class, and the child class adds additional functionality.

---

