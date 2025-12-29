**What is Python?** Python is a high-level, general-purpose, interpreted programming language designed for readability and productivity. It uses significant indentation for blocks, supports multiple paradigms (procedural, OOP, functional) and comes with a large standard library. Python is dynamically typed and garbage-collected, making it easy to write and maintain code.

## 1. What does **Dynamically Typed** mean?

**Dynamic typing** means:

> You do **not** need to declare the data type of a variable in advance.  
> Python decides the type **at runtime** (while the program is running).

### Example:

`x = 10       # x is an integer x = "Hello"  # now x becomes a string x = 3.14     # now x becomes a float`

Here:

- You never wrote `int x` or `string x`
    
- Python automatically assigns the type based on the value
### In contrast (Statically typed languages like C/Java):

`int x = 10; x = "Hello";  // ❌ Error`

### Advantages:

- Faster coding
    
- Less boilerplate
    
- More flexible

### Disadvantages:

- Errors may appear **at runtime**, not compile time
---

## 2. What does **Garbage Collected** mean?

**Garbage collection** means:

> Python automatically frees memory that is no longer being used by the program.

You **don’t need to manually delete memory**.

---

### Example:

`a = 100 b = a del a`

- Memory is still used because `b` refers to it
    
- When **no variable refers to that object**, Python deletes it automatically
    

---

### How Python does Garbage Collection:

Python mainly uses:

1. **Reference Counting**
    
2. **Cyclic Garbage Collector**
---
- **Dynamic Typing:**  
    Python determines variable data types at runtime, allowing variables to change types without explicit declarations.
    
- **Garbage Collection:**  
    Python automatically manages memory by freeing objects that are no longer referenced, preventing memory leaks.
---

### **Boilerplate** means:

> **Repetitive, standard code that must be written every time but does not add new logic or functionality.**
### 🔹 Java (More Boilerplate)

`public class Main {     public static void main(String[] args) {         System.out.println("Hello World");     } }`

Here, most of the code is boilerplate just to run one line.

---
### 🔹 Python (Less Boilerplate)
`print("Hello World")`
Python removes unnecessary boilerplate.

---
## Why Boilerplate Exists 
- Enforces structure
- Improves readability in large systems
- Helps compilers and frameworks

---

# Why Python is Popular
- Minimal boilerplate
- Faster development
- Cleaner, readable code
---
**Is Python compiled or interpreted?** Python is usually described as an _interpreted_ language: the source code is compiled to bytecode and executed by the Python interpreter at runtime. In practice, Python code is not directly converted to machine code ahead of time – it runs via an interpreter (CPython, PyPy, etc.) which means syntax and runtime errors typically appear when executing the program.

**What are common applications of Python?** Python’s versatility makes it suitable for many fields. For example, it’s used in **web development** (frameworks like Django and Flask), **data science and machine learning** (libraries such as NumPy, pandas, scikit-learn, TensorFlow), **scripting and automation** (system administration scripts, task automation), **desktop GUI** (Tkinter, PyQt), **game development** (Pygame), and education due to its readability. In scientific and numeric computing, Python’s powerful libraries make it ideal for research and simulations.

---
# Whats the difference between method, function, framework and library*
## 1. Function
A **function** is a block of reusable code that performs a specific task.  
It is **independent** and not tied to any object.
### Example (Python):

`def add(a, b):     return a + b`

---
## 2. Method
A **method** is a function that **belongs to a class or object**.  
It operates on the data (attributes) of that object.
### Example:

`class Calculator:     def add(self, a, b):         return a + b`
Usage:
`calc = Calculator() calc.add(2, 3)`

📌 Methods are called **through objects**.

---
## 3. Library
A **library** is a **collection of functions, classes, and modules** that help you perform common tasks.  
👉 **You control the flow** of the program.
### Example:

- Python standard library: `math`, `os`, `datetime`
- Third-party libraries: `NumPy`, `Pandas`

`import math print(math.sqrt(16))`

📌 You **call the library** when you need it.

---
## 4. Framework
A **framework** is a **complete structure** for building applications.  
👉 **The framework controls the flow**, not you (**Inversion of Control**).
### Example:
- Web frameworks: `Django`, `Flask`, `Spring`
- ML frameworks: `TensorFlow`, `PyTorch`

`# Django example (simplified) def home(request):     return HttpResponse("Hello")`

📌 The framework decides:
- When your code runs
- How components interact

---

## Key Difference: Library vs Framework (Very Important)

|Feature|Library|Framework|
|---|---|---|
|Control flow|You control|Framework controls|
|Usage|You call it|It calls your code|
|Scope|Specific tasks|Full application structure|
|Flexibility|High|More opinionated|

---

## Quick Comparison Table

|Term|What it is|Example|
|---|---|---|
|Function|Independent block of code|`len()`|
|Method|Function inside a class|`list.append()`|
|Library|Collection of functions/classes|`NumPy`|
|Framework|Complete app structure|`Django`|

---

## One-Line Definitions (Perfect for Exams)

- **Function:** A reusable block of code that performs a specific task.
- **Method:** A function associated with an object or class.
- **Library:** A collection of reusable code that the programmer calls.
- **Framework:** A structured platform that controls application flow and calls user code.
---
# 1. What is a Library? (Baseline)

A **library** is a collection of reusable code that helps you perform **specific tasks**.  
You **control the flow** of the program.
### Examples:
- `requests` → HTTP requests
- `NumPy` → numerical computation
- `Pandas` → data analysis

`import requests response = requests.get("https://api.example.com")`

---
# 2. Flask (Micro Framework)

**Flask** is a **lightweight web framework**.  
It provides only the **core features** needed to build a web app.

### Features:
- URL routing
- Request/response handling
- Jinja2 templates
- Very flexible
### Example:

`from flask import Flask app = Flask(__name__)  @app.route("/") def home():     return "Hello Flask"`

📌 You choose extra libraries for:

- Database (SQLAlchemy)
- Authentication
- Forms
- Validation
---
# 3. Django (Full-Stack Framework)

**Django** is a **batteries-included framework**.  
It provides **almost everything out of the box**.
### Features:
- ORM (database handling)
- Authentication
- Admin panel
- Security (CSRF, SQL injection)
- URL routing & templates
---
### ✅ Use **Flask** when:
- Small web apps or APIs
- Microservices
- You want full control
- Learning web development
---
### ✅ Use **Django** when:
- Large, production-level apps
- Authentication, admin, security needed
- Rapid development with standard structure
- Teams and scalability matter
---

**What are basic Python data types?**
Python’s built-in types include **numeric types** (`int`, `float`, `complex`), **sequence types** (`str` for text, `list`, `tuple`, `range`), **mapping type** (`dict`), **set types** (`set`, `frozenset`), **boolean** (`bool`), and **binary types** (`bytes`, `bytearray`, `memoryview`). For example, `x = 42` creates an `int`, `s = "hello"` is a `str`, and `L = [1,2,3]` is a `list`.

**What is the difference between a list and a tuple?** 
A **list** is a mutable sequence (defined with `[...]`) whose elements can be changed, appended or removed after creation. A **tuple** is an immutable sequence (defined with `(...)` or no brackets) which cannot be modified once created. In other words, lists are variable-length and changeable, whereas tuples are fixed-size. Because tuples are immutable, they can be used as dictionary keys, whereas lists cannot.

**What is a Python list and how is it different from an array?** 
A Python list is a dynamic, heterogeneous container (elements can be of different types) and can grow or shrink as needed. Python also has an `array` module and third-party array types (like NumPy’s `ndarray`) which require fixed data types for performance. In general, use a **list** for general-purpose collections; use specialized arrays (e.g. NumPy arrays) when you need efficient storage and computation on large numeric datasets.

**How do you install external Python packages?** The standard way is using the **`pip`** package manager. For example, to install the NumPy library you would run `pip install numpy` which downloads the package from PyPI and installs it into your environment. You can also specify versions (e.g. `pip install package==1.2.3`) and upgrade or uninstall packages using `pip`.

**What is a virtual environment and why use it?** A virtual environment (created via `python -m venv env`) is an isolated Python environment with its own interpreter and libraries. It ensures that dependencies for one project don’t conflict with others. Each virtual env has its own site-packages directory, so you can install different versions of packages per project. This helps avoid “dependency hell” and makes projects reproducible.

**What is a Python dictionary?** A **dictionary** is an _unordered_ collection of key:value pairs. You can think of it as a mapping or “address-book” where each unique key maps to a value. For example, `d = {"apple": 3, "banana": 5}` maps `"apple"` to `3` etc. Dictionaries provide fast lookup by key and are defined using `{}` or the `dict()` constructor. (Keys must be immutable types.)

**How do `if`, `elif`, `else` statements work?** These are Python’s conditional blocks. Example:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6|`if` `condition1:`<br><br>    `# code block A`<br><br>`elif` `condition2:`<br><br>    `# code block B`<br><br>`else``:`<br><br>    `# code block C`|

The first true condition’s block executes, and the rest are skipped. Indentation is mandatory to delimit the blocks. Comparison operators (`==`, `<`, `>`, etc.) and logical operators (`and`, `or`, `not`) are used in the condition expressions.

**What loops are available in Python?** Python has `for` loops and `while` loops. A `for` loop iterates over a sequence (list, string, tuple, dict keys, etc.), for example:

|   |   |
|---|---|
|1<br><br>2|`for` `x` `in` `[``1``,``2``,``3``]:`<br><br>    `print``(x)`|

A `while` loop repeats as long as a condition is true:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4|`i` `=` `0`<br><br>`while` `i <` `5``:`<br><br>    `print``(i)`<br><br>    `i` `+``=` `1`|
Inside loops, `break` exits the loop, and `continue` skips to the next iteration.

---
**How do you use the `range()` function in loops?** The `range(start, stop, step)` function generates an integer sequence. It’s commonly used with `for`. For example, `range(5)` yields 0,1,2,3,4. You can specify a `start` (default 0) and a `step`. Example: `for i in range(2, 10, 2):` iterates over 2, 4, 6, 8. The `stop` value is exclusive.

**Why is indentation important in Python?** Unlike languages with braces, Python uses **significant indentation** to define code blocks. All statements within the same block must have the same indentation. Mis-indented code will raise an `IndentationError`. Proper indentation improves readability, which is part of Python’s design philosophy.

**What is `__init__()` in a Python class?** The `__init__` method is the class initializer (often called the constructor). It’s automatically invoked when an instance is created. In `__init__`, you typically assign attributes. For example:

|   |   |
|---|---|
|1<br><br>2<br><br>3|`class` `Dog:`<br><br>    `def` `__init__(``self``, name):`<br><br>        `self``.name` `=` `name`|

Here, creating `d = Dog("Fido")` automatically calls `Dog.__init__(d, "Fido")`, setting `d.name`. The `__init__` method can take additional parameters for initialization.

**What is `self` in Python class methods?** In Python, `self` refers to the current instance of the class. It is used inside methods to access attributes and other methods on the object. You always include `self` as the first parameter of instance methods. For example:

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5|`class` `Example:`<br><br>    `def` `__init__(``self``, value):`<br><br>        `self``.value` `=` `value` `# 'self.value' is an attribute of this object`<br><br>    `def` `show(``self``):`<br><br>        `print``(``self``.value)` `# using 'self' to access the attribute`|

When you call `obj = Example(5); obj.show()`, Python automatically passes `obj` as `self`.


**How does exception handling work?** Python uses `try`/`except` blocks to catch and handle errors. Example:

|                                                |                                                                                                                                                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6 | `try``:`<br><br>    `risky_operation()`<br><br>`except` `(TypeError, ValueError) as e:`<br><br>    `print``(``"Error:"``, e)`<br><br>`finally``:`<br><br>    `print``(``"Cleanup code runs no matter what"``)` |

Code in the `try` block is attempted; if an exception occurs, control jumps to the matching `except`. You can catch specific exceptions. The optional `finally` block executes regardless of whether an error occurred. This prevents crashes and allows graceful error handling.

**What is a module and what is a package?** A **module** is a single Python file (`.py`) that contains definitions (functions, classes, variables) which you can import into other code. A **package** is a directory containing a special `__init__.py` file and possibly multiple modules or subpackages. Packages help organize related modules. You import them using `import module_name` or `from package import submodule`.

# **What are positional vs keyword arguments in functions?
## 1. Positional Arguments

**Positional arguments** are passed to a function **based on their position (order)**.
`def introduce(name, age):     print(name, age)  introduce("Lalit", 22)`
✔ `"Lalit"` → `name`  
✔ `22` → `age`

Order matters:
`introduce(22, "Lalit")  # Wrong meaning`
## 2. Keyword Arguments
**Keyword arguments** are passed using **parameter names**, so **order does not matter**.
### Example:
`introduce(age=22, name="Lalit")`
✔ Correct even though order is changed  
✔ More readable and safer

---
## 3. Mixing Positional and Keyword Arguments
You **can mix**, but:
> **Positional arguments must come first**
### Valid:
`introduce("Lalit", age=22)`
### Invalid:
`introduce(name="Lalit", 22)  # ❌ Error`

---

## 4. Default Arguments (Related Concept)
You can assign **default values** to parameters.
`def greet(name, message="Hello"):     print(message, name)  greet("Lalit") greet("Lalit", message="Hi")`

---
## 6. Interview / Exam One-Line Answers
- **Positional arguments:**  
    Arguments passed to a function based on their position in the function call.
- **Keyword arguments:**  
    Arguments passed using parameter names, making order irrelevant.
---

# 1. `*args` (Variable Positional Arguments)

`*args` allows a function to accept **any number of positional arguments**.
### Example:
`def add(*args):     return sum(args)  add(1, 2) add(1, 2, 3, 4)`
- `args` is a **tuple**
- Name can be anything, but `args` is a convention
---
# 2. `**kwargs` (Variable Keyword Arguments)

`**kwargs` allows a function to accept **any number of keyword arguments**.
### Example:
`def student_info(**kwargs):     for key, value in kwargs.items():         print(key, value)  student_info(name="Lalit", age=22, course="CSE")`

- `kwargs` is a **dictionary**
- Used when keys are not fixed
`*args` allows a function to accept variable positional arguments as a tuple, while `**kwargs` allows variable keyword arguments as a dictionary.
---
**What is a list comprehension?** A list comprehension is a concise way to create lists using a single expression. Syntax example: `[expr(x) for x in iterable if condition(x)]`. For instance, `[n*n for n in range(5)]` produces `[0,1,4,9,16]`. It is generally more readable and often faster than an equivalent `for` loop. Comprehensions can include an optional `if` to filter items, e.g. `[n for n in range(10) if n%2==0]` for even numbers.

**What is a generator expression and how is it different from a list comprehension?** A generator expression is similar to a list comprehension but uses parentheses instead of brackets. For example: `gen = (x*x for x in range(5))`. This creates a generator object that **yields** values one at a time, instead of building the entire list in memory. In contrast, a list comprehension would build and return the full list immediately. Generator expressions are memory-efficient for large data. In short, list comprehensions return a full list, while generator expressions return an iterator that produces items on demand.

**What are `map()`, `filter()`, and `reduce()`?** These are built-in functions (with `reduce` in `functools`) from functional programming.

- `map(function, iterable)` applies the function to each item of the iterable and returns an iterator of results.
- `filter(function, iterable)` yields only the items for which the function returns True.
- `functools.reduce(function, sequence)` applies a binary function cumulatively to the items of the sequence, reducing it to a single value (e.g. summing a list). They allow concise data transformations without explicit loops.

**Which testing tools/frameworks are available in Python?** The standard library provides `unittest`, a rich framework for unit testing (with test cases and suites). A popular third-party tool is **pytest**, which has a simpler syntax (just write `assert` statements) and powerful features like fixtures. There’s also `nose` (less maintained) and `doctest` (inline tests in docstrings). In practice, many developers use `pytest` for its ease of use.

**What is `__name__ == "__main__"` used for?** In a Python file, the special variable `__name__` is set to `"__main__"` when the file is executed as the main program, and to the module name when imported. So you often see:

|   |   |
|---|---|
|1<br><br>2|`if` `__name__` `=``=` `"__main__"``:`<br><br>    `main()`|

This ensures that the code under this `if` only runs when the script is executed directly, not when it is imported as a module. It’s a common pattern to allow a file to be both used as a script and as an importable module.

**What is `dir()` and `help()`?** `dir(object)` is a built-in that lists the attributes and methods of an object (module, class, instance, etc.). It’s useful for introspection. `help(object)` or `help("keywords")` invokes Python’s help system, showing documentation for the object or topic. These interactive functions help explore code and find available methods or documentation.

**What is slicing in Python?** Slicing allows you to extract a subsequence from sequences (lists, strings, tuples). The syntax is `sequence[start:stop:step]`. For example, `s = "Hello"; s[1:4]` gives `"ell"` (indices 1 through 3). Leaving out indices means default start/end, and a negative step (e.g. `s[::-1]`) can reverse the sequence. Slicing is a concise way to manipulate parts of sequences and is very efficient.

**What is slicing in Python?** Slicing allows you to extract a subsequence from sequences (lists, strings, tuples). The syntax is `sequence[start:stop:step]`. For example, `s = "Hello"; s[1:4]` gives `"ell"` (indices 1 through 3). Leaving out indices means default start/end, and a negative step (e.g. `s[::-1]`) can reverse the sequence. Slicing is a concise way to manipulate parts of sequences and is very efficient.

**What is the difference between `==` and `is`?** The `==` operator checks _equality of value_, i.e., whether two objects have the same value. The `is` operator checks _identity_, i.e., whether two references point to the exact same object in memory. For example, two separate lists with identical contents are `==` but not `is`. Generally use `==` for value comparison and `is` only to check for the same object (often used for `None`, e.g. `if x is None`).

https://www.javacodegeeks.com/python-interview-questions.html
