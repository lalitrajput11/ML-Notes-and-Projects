![[Pasted image 20251215082609.png]]
tIME: MTH :- BBISTQ:- 

![](https://miro.medium.com/v2/resize:fit:656/0*BBuwfCVvp_pRipWr.png)

### 1. Time Complexity

**Time complexity** measures the amount of time an algorithm takes to complete as a function of the input size. It’s a way to estimate the running time of an algorithm.

- **Big O Notation (O-notation)**: This is used to describe the upper bound of an algorithm’s running time. It tells you how the runtime scales with the size of the input.
- **O(1)**: Constant time. The running time doesn’t change with the input size. Example: Accessing an array element by index.
- **O(log n)**: Logarithmic time. The running time increases logarithmically as the input size increases. Example: Binary search in a sorted array.
- **O(n)**: Linear time. The running time increases linearly with the input size. Example: Iterating through an array.
- **O(n log n)**: Log-linear time. Common in efficient sorting algorithms like mergesort and quicksort.
- **O(n²)**: Quadratic time. The running time grows quadratically with the input size. Example: Nested loops, such as in bubble sort.
- **O(2^n)**: Exponential time. The running time doubles with each additional input element. Example: Recursive algorithms solving the Towers of Hanoi.
- **O(n!)**: Factorial time. The running time grows factorially with the input size. Example: Brute-force solutions to the traveling salesman problem.


![](https://miro.medium.com/v2/resize:fit:656/0*BBuwfCVvp_pRipWr.png)

### 1. Time Complexity

**Time complexity** measures the amount of time an algorithm takes to complete as a function of the input size. It’s a way to estimate the running time of an algorithm.

- **Big O Notation (O-notation)**: This is used to describe the upper bound of an algorithm’s running time. It tells you how the runtime scales with the size of the input.
- **O(1)**: Constant time. The running time doesn’t change with the input size. Example: Accessing an array element by index.
- **O(log n)**: Logarithmic time. The running time increases logarithmically as the input size increases. Example: Binary search in a sorted array.
- **O(n)**: Linear time. The running time increases linearly with the input size. Example: Iterating through an array.
- **O(n log n)**: Log-linear time. Common in efficient sorting algorithms like mergesort and quicksort.
- **O(n²)**: Quadratic time. The running time grows quadratically with the input size. Example: Nested loops, such as in bubble sort.
- **O(2^n)**: Exponential time. The running time doubles with each additional input element. Example: Recursive algorithms solving the Towers of Hanoi.
- **O(n!)**: Factorial time. The running time grows factorially with the input size. Example: Brute-force solutions to the traveling salesman problem.

**Key Points**:

- **Best Case**: The scenario where the algorithm performs the minimum number of steps.
- **Worst Case**: The scenario where the algorithm performs the maximum number of steps.
- **Average Case**: The expected scenario, considering all possible inputs.

### 2. Space Complexity

**Space complexity** measures the amount of memory an algorithm uses as a function of the input size.

- **Big O Notation for Space Complexity**: Just like time complexity, space complexity can be expressed in Big O notation.
- **O(1)**: Constant space. The algorithm uses a fixed amount of memory regardless of input size. Example: Variables storing sums or counters.
- **O(n)**: Linear space. The memory usage grows linearly with the input size. Example: Storing an additional array or list.
- **O(n²)**: Quadratic space. The memory usage grows quadratically with the input size. Example: Storing a 2D matrix.

**Key Points**:

- **Auxiliary Space**: The extra space or temporary space used by an algorithm.
- **In-place Algorithm**: An algorithm that uses a constant amount of extra space, typically O(1).

## 3. Analyzing Time and Space Complexity for Code

Let’s take a simple example:

int sumArray(int arr[], int n) {  
    int sum = 0;  // O(1) space  
    for (int i = 0; i < n; i++) {  // O(n) time  
        sum += arr[i];  // O(1) time  
    }  
    return sum;  // O(1) time  
}

- **Time Complexity**:
- The loop runs `n` times, so the time complexity is O(n).
- Inside the loop, addition and access operations are O(1).
- Overall, time complexity: **O(n)**.
- **Space Complexity**:
- The only additional space used is the `sum` variable, which is O(1).
- Overall, space complexity: **O(1)**.

## 4. Interview Perspective

When asked about time and space complexity in an interview:

- **Understand the Code**: Break it down into loops, recursive calls, and space usage.
- **Identify Key Operations**: Focus on loops, recursive functions, and how data structures (arrays, lists, etc.) grow.
- **Express in Big O Notation**: Clearly state the time and space complexity using Big O notation.
- **Compare Alternatives**: If possible, discuss more efficient alternatives or why a particular complexity is necessary.

## 5. Big O Notation in Detail

- **Upper Bound**: Big O gives the worst-case scenario (maximum time taken).
- **Ignore Constants**: In Big O notation, coefficients and lower-order terms are ignored because they don’t significantly impact growth rates as input size increases.
- For example, O(2n + 5) simplifies to O(n).

## 6. Common Patterns:

- **Single Loop**: O(n) time, O(1) space.
- **Nested Loop**: O(n²) time, O(1) space.
- **Recursive Calls**: Depends on the depth and breadth of recursion. Often O(2^n) or O(n!).
- 
**Key Points**:

- **Best Case**: The scenario where the algorithm performs the minimum number of steps.
- **Worst Case**: The scenario where the algorithm performs the maximum number of steps.
- **Average Case**: The expected scenario, considering all possible inputs.

### 2. Space Complexity

**Space complexity** measures the amount of memory an algorithm uses as a function of the input size.

- **Big O Notation for Space Complexity**: Just like time complexity, space complexity can be expressed in Big O notation.
- **O(1)**: Constant space. The algorithm uses a fixed amount of memory regardless of input size. Example: Variables storing sums or counters.
- **O(n)**: Linear space. The memory usage grows linearly with the input size. Example: Storing an additional array or list.
- **O(n²)**: Quadratic space. The memory usage grows quadratically with the input size. Example: Storing a 2D matrix.

**Key Points**:

- **Auxiliary Space**: The extra space or temporary space used by an algorithm.
- **In-place Algorithm**: An algorithm that uses a constant amount of extra space, typically O(1).
### Key Concepts and Explanations

#### 1. **What is Time Complexity?**

- Time complexity is **not the actual time in seconds** taken by a program to run, because runtime varies with hardware, system, and other factors.
- **Correct definition:** Time complexity measures the **rate of increase in time** taken by the code as the input size grows.
- Example: If a program takes 1 second for 500 inputs and 2 seconds for 1000 inputs, the time complexity reflects this growing trend, not the absolute time.
- Time complexity is expressed in terms of input size **n**, for example, `3n` means the time grows linearly with input size.

#### 2. **Types of Time Complexities**

- **Big O Notation (O):** Represents the **worst-case time complexity** or upper bound.
- **Omega (Ω):** Represents the best-case time complexity or lower bound.
- **Theta (Θ):** Represents the average case (between best and worst).
- Interviews generally focus on **Big O notation (worst-case)** since it guarantees performance under the most demanding conditions.

#### 3. **Rules for Calculating Time Complexity**

- Always calculate time complexity based on the **worst-case scenario**.
- **Ignore constant values** and lower order terms as they become insignificant for large inputs.
- Focus on the **dominant term** that grows fastest with input size.

---

---

### Space Complexity

- Space complexity measures the **extra memory** a program uses relative to the input size.
- It includes:
    - **Input space:** Memory required to store the input.
    - **Auxiliary space:** Extra memory used to solve the problem (e.g., additional variables, data structures).
- Example: Adding three numbers using one extra variable `total` has:
    - Input space = 3 (for three numbers)
    - Auxiliary space = 1 (for the `total` variable)
- Modification of input data without explicit permission is discouraged; auxiliary space should be counted separately.
- Space complexity is also expressed using **Big O notation**, e.g., O(n) for storing an array of size n.
## 3. Analyzing Time and Space Complexity for Code

Let’s take a simple example:

int sumArray(int arr[], int n) {  
    int sum = 0;  // O(1) space  
    for (int i = 0; i < n; i++) {  // O(n) time  
        sum += arr[i];  // O(1) time  
    }  
    return sum;  // O(1) time  
}

- **Time Complexity**:
- The loop runs `n` times, so the time complexity is O(n).
- Inside the loop, addition and access operations are O(1).
- Overall, time complexity: **O(n)**.
- **Space Complexity**:
- The only additional space used is the `sum` variable, which is O(1).
- Overall, space complexity: **O(1)**.

## 4. Interview Perspective

When asked about time and space complexity in an interview:

- **Understand the Code**: Break it down into loops, recursive calls, and space usage.
- **Identify Key Operations**: Focus on loops, recursive functions, and how data structures (arrays, lists, etc.) grow.
- **Express in Big O Notation**: Clearly state the time and space complexity using Big O notation.
- **Compare Alternatives**: If possible, discuss more efficient alternatives or why a particular complexity is necessary.

## 5. Big O Notation in Detail

- **Upper Bound**: Big O gives the worst-case scenario (maximum time taken).
- **Ignore Constants**: In Big O notation, coefficients and lower-order terms are ignored because they don’t significantly impact growth rates as input size increases.
- For example, O(2n + 5) simplifies to O(n).

## 6. Common Patterns:

- **Single Loop**: O(n) time, O(1) space.
- **Nested Loop**: O(n²) time, O(1) space.
- **Recursive Calls**: Depends on the depth and breadth of recursion. Often O(2^n) or O(n!).

## Search 


|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**Algorithm**|**Best Case**|**Average Case**|**Worst Case**|**Works On**|**Space Complexity**|
|Linear Search|O(1)|O(n)|O(n)|Unsorted data|O(1)|
|Binary Search|O(1)|O(log n)|O(log n)|Sorted array|O(1)|
|Hash Search|O(1)|O(1)|O(n)|Key-value pairs|O(n)|
|Tree Search (BST)|O(log n)|O(log n)|O(n)|Tree structure|O(n)|
|Interpolation|O(1)|O(log log n)|O(n)|Sorted, uniform|O(1)|
### Applications of Searching Algorithms :-

Search Engines: Keyword lookup and index retrieval.
Databases: Query processing, record lookup.
E-commerce Platforms: Product search, filtering.
Operating Systems: File search, memory management.
Artificial Intelligence: Pathfinding algorithms (e.g., A* search).

---
---
---
