The term “Object-Oriented Programming” (OOP), also known as OOPs principles in python, was coined by Alan Kay around 1966 while he was at grad school. The language called **Simula** was the first programming language with the features of Object-oriented programming. It was developed in 1967 for making [**simulation programs**](https://en.wikipedia.org/wiki/Computer_simulation), in which the most important information was called objects.

Though OOPs were in the market since the early 1960s it was in the 1990s that OOPs began to grow because of C++.

## What Is Object-Oriented Programming (OOPs) in python?

In Python, OOPs stands for Object-Oriented Programming. It is a programming paradigm that focuses on the use of objects and classes to create programs. An object is a group of interrelated variables and functions. These variables are often referred to as properties of the object, and functions are referred to as the behavior of the objects. These objects provide a better and clear structure for the program. Main principles of OOPs in Python are abstraction, encapsulation, inheritance, and polymorphism.
### Core Concepts Covered


- **Object-Oriented Programming (OOP):**  
    Defined as a programming paradigm centered around **objects** which are instances of **classes**. OOP enables the creation of custom data types and models real-world entities effectively.
    
- **Classes and Objects:**
    
    - A **class** is a blueprint or template defining properties (data members) and behaviors (methods).
    - An **object** is an instance of a class with specific values and state. Each object has a unique reference (ID).
    - Objects interact via methods, and data encapsulation ensures controlled access.
- **Attributes and Methods:**
    
    - **Attributes** store data/state about an object.
    - **Methods** define the object’s behaviors and can manipulate the object’s data.
- **Constructor (`__init__` method):**  
    A special method automatically called when an object is instantiated to initialize attributes.
    
- **Self Parameter:**  
    Refers to the current object instance, enabling access to its attributes and methods.
    
- **Data Encapsulation and Access Modifiers:**
    
    - Use of naming conventions like **single or double underscores** to indicate protected or private members.
    - Python does not enforce strict private members but follows conventions to discourage direct access.
    
- **Inheritance:**
    
    - Mechanism by which a **child class inherits properties and methods** from a **parent class**, facilitating code reuse and hierarchical relationships.
    - Types include **single inheritance**, **multilevel inheritance**, **multiple inheritance** (supported in Python), and **hybrid inheritance** (combination).
- **Polymorphism:**
    
    - Ability of methods to behave differently based on the calling object or parameters.
    - Includes concepts like **method overriding** (child class method replaces parent class method) and **operator overloading** (customizing operators like `+`).
- **Method vs Function:**
    
    - **Functions** are general and defined outside classes.
    - **Methods** are functions defined inside classes and operate on objects.
- **Magic Methods (Dunder Methods):**  
    Special methods in Python (identified by double underscores prefix and suffix, e.g., `__init__`, `__str__`) that provide built-in behavior for objects, like object creation, printing, operator overloading.
    

---

### Practical Examples and Use Cases

1. **ATM Management System:**
    
    - Classes represent ATM, Customer, and operations like checking balance, deposit, and withdrawal.
    - Demonstrates encapsulation (hiding PIN and balance), validation, and method calls.
    - Shows how constructors initialize customer data and how methods manipulate state securely.
2. **Fraction Class:**
    
    - Custom data type created to handle fractions with operations like addition, subtraction, multiplication, and division.
    - Implements operator overloading for arithmetic operations using magic methods.
3. **Inheritance Example:**
    
    - Parent class representing a generic user or product.
    - Child classes like Student, Inspector, Smartphone inheriting from parent classes to extend or modify behavior.
    - Demonstrates method overriding and the use of `super()` to call parent class methods.
4. **Train Status Application (IRCTC API):**
    
    - Illustrates fetching real-time train data via API requests using Python’s `requests` library.
    - Parses complex JSON/dictionary responses to extract information like station names, arrival/departure times, and distance.
    - Shows practical application of classes and methods to build real-world software.

---

### Important Highlights and Best Practices

- **Code Reusability:** Using inheritance to avoid code duplication and increase maintainability.
- **Data Security:** Properly hiding sensitive data like PINs using naming conventions and providing getter-setter methods for controlled access.
- **Magic Methods:** Automate behaviors such as object initialization and operator overloading, making class objects behave like built-in types.
- **Polymorphism:** Enables flexible and dynamic method behavior, crucial for designing scalable software.
- **Aggregation:** Demonstrated by passing objects as attributes within other objects (e.g., Customer object contains Address object).
- **Use of Static/Class Variables:** For shared data across all instances, e.g., serial number counters for objects.
- **Managing Mutable vs Immutable Objects:** Emphasized caution when passing mutable objects (like lists) to functions to avoid unintended side effects.
- **Clear Naming Conventions:** Classes use **CamelCase**, variables and methods use **snake_case** for readability and consistency.
- **Avoiding Code Repetition:** Demonstrated through inheritance and modular design to follow DRY (Don’t Repeat Yourself) principles.

---

### Definitions and Comparisons in Markdown Table

|Term|Definition/Description|Example/Notes|
|---|---|---|
|Class|Blueprint/template defining data and behavior|`class ATM:`|
|Object|Instance of a class with specific data|`atm1 = ATM()`|
|Method|Function defined inside a class|`def deposit(self, amount):`|
|Constructor|Special method `__init__` initializing object attributes|Called automatically on object creation|
|Self|Reference to current object instance|Used as first parameter in methods|
|Encapsulation|Hiding data and restricting direct access|Using underscore prefix `_balance`|
|Inheritance|Child class inherits properties/methods of parent class|`class Student(User):`|
|Polymorphism|Same method behaves differently based on object/parameters|Method overriding in child class|
|Magic Method|Special predefined methods with double underscores|`__init__`, `__str__`, `__add__`|
|Aggregation|Object contains another object as attribute|`Customer` has `Address` object|
|Operator Overloading|Defining behavior of operators for custom objects|Overloading `+` for fraction class|
|Static Variable|Shared variable among all instances of a class|Serial number counter|

### Key Insights and Conclusions

- **Understanding OOP fundamentals is crucial for building scalable and maintainable software.**
- Python treats everything as an object, even basic data types like integers and lists.
- Creating custom classes allows the modeling of real-world problems with tailored data and behavior.
- Proper use of constructors, encapsulation, and methods leads to cleaner, more secure code.
- Inheritance and polymorphism help reduce code redundancy and enable flexible code reuse.
- Magic methods empower Python classes to integrate seamlessly with built-in operations and syntax.
- Practical examples like ATM systems and train status apps demonstrate the real-world applicability of OOP concepts.
- Managing mutable objects and references carefully prevents bugs related to unintended data changes.
- Design patterns like aggregation and the use of static variables enhance class design and object management.
- Operator overloading and method overloading provide sophisticated control over class behavior but require careful implementation.
- API integration (like Indian Railways API) showcases how OOP and Python can be used to build functional applications fetching and processing live data.