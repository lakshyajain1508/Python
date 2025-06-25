# Abstract Classes

**Introduction to Abstract Classes**

Abstract classes in Python are a way to define a blueprint for other classes. They are classes that contain one or more abstract methods, which are methods that are declared but contain no implementation. Abstract classes cannot be instantiated directly and are intended to be subclassed, with the subclasses providing concrete implementations of the abstract methods.

Python provides the `abc` (Abstract Base Class) module to define abstract classes and methods. This tutorial will cover the concept of abstract classes, their purpose, and how to use them effectively in Python.

**Key Concepts:**
1. **What is an Abstract Class?**
2. **Defining Abstract Classes**
3. **Creating Abstract Methods**
4. **Concrete Methods in Abstract Classes**
5. **Subclassing Abstract Classes**
6. **Using `@abstractmethod` Decorator**
7. **Benefits of Abstract Classes**
8. **Abstract Classes vs Interfaces**
9. **Practical Examples of Abstract Classes**
10. **Best Practices for Using Abstract Classes**

### **1. What is an Abstract Class?**

An abstract class is a class that cannot be instantiated and typically includes one or more abstract methods. Abstract methods are methods that are declared in the abstract class but do not contain any implementation. Subclasses of the abstract class are responsible for providing concrete implementations of these methods.

Abstract classes allow you to define a common interface for a group of related classes, ensuring that all subclasses implement specific methods.

#### **Example:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

In this example, `Shape` is an abstract class that defines two abstract methods: `area` and `perimeter`. Any subclass of `Shape` must implement these methods.

### **2. Defining Abstract Classes**

To define an abstract class in Python, you need to inherit from the `ABC` class, which stands for Abstract Base Class. The `ABC` class is provided by the `abc` module.

#### **Example:**

```python
from abc import ABC

class Vehicle(ABC):
    def start_engine(self):
        pass
```

Here, `Vehicle` is an abstract class that inherits from `ABC`. Although this class does not define any abstract methods, it can still serve as a base class for other classes.

### **3. Creating Abstract Methods**

Abstract methods are methods that are declared in an abstract class but have no implementation. They are defined using the `@abstractmethod` decorator from the `abc` module.

#### **Example:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

In this example, the `Animal` class defines an abstract method `make_sound`. Any subclass of `Animal` must provide an implementation of the `make_sound` method.

### **4. Concrete Methods in Abstract Classes**

Abstract classes can also contain concrete methods, which are methods with an implementation. These methods can be used by subclasses without needing to be overridden.

#### **Example:**

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    @abstractmethod
    def calculate_bonus(self):
        pass
```

In this example, `Employee` is an abstract class that defines a concrete method `get_details` and an abstract method `calculate_bonus`. Subclasses must implement `calculate_bonus`, but they can use the `get_details` method as is.

### **5. Subclassing Abstract Classes**

When you create a subclass of an abstract class, you must provide concrete implementations for all abstract methods. If a subclass does not implement all abstract methods, it remains abstract and cannot be instantiated.

#### **Example:**

```python
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20
```

In this example, `Developer` and `Manager` are subclasses of `Employee`. Both classes provide their own implementations of the `calculate_bonus` method, fulfilling the requirements of the abstract class.

### **6. Using `@abstractmethod` Decorator**

The `@abstractmethod` decorator is used to mark methods as abstract. This decorator enforces that the method must be overridden in any subclass.

#### **Example:**

```python
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
```

In this example, the `@abstractmethod` decorator is used to define two abstract methods, `turn_on` and `turn_off`, which must be implemented by any subclass of `Appliance`.

### **7. Benefits of Abstract Classes**

- **Encourages Code Reusability:** Abstract classes allow you to define a common interface for related classes, promoting code reusability.
- **Enforces Method Implementation:** Abstract classes ensure that specific methods are implemented in all subclasses, providing a consistent interface.
- **Improves Code Organization:** By defining common functionality in an abstract class, you can keep your code organized and reduce duplication.
- **Enhances Readability:** Abstract classes make it clear what methods must be implemented in subclasses, improving the readability and maintainability of your code.

### **8. Abstract Classes vs Interfaces**

In Python, abstract classes and interfaces serve similar purposes, but they have some differences:

- **Abstract Classes:** Can contain both abstract and concrete methods. They allow you to define shared behavior that can be inherited by subclasses.
- **Interfaces (in other languages):** Typically contain only abstract methods and no implementation. Python doesn't have a dedicated interface keyword, but abstract classes can be used to achieve similar functionality.

### **9. Practical Examples of Abstract Classes**

**Example 1: Payment Processing System**

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Using the classes
payment = CreditCardProcessor()
payment.process_payment(100)
```

**Example 2: Vehicle System**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# Using the classes
vehicle = Car()
vehicle.start_engine()
```

---
