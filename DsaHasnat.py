QSN1:?
ANS:
Binary Search
Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed the possible locations to just one.

*Code*
```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)
print(f"Target {target} found at index {index}" if index != -1 else f"Target {target} not found")
```

Linear Search
Linear Search is a simple algorithm for finding an item from a list of items. It works by iterating through the list and checking each item until it finds the desired item.

*Code*
```
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = linear_search(arr, target)
print(f"Target {target} found at index {index}" if index != -1 else f"Target {target} not found")
```
*Time Complexity*
- Binary Search: O(log n)
- Linear Search: O(n)

 :QSN:2 How to run the program?
ANS:
1. Install Python.
2. Copy the code.
3. Save the file with a `.py` extension.
4. Run the program using `python filename.py`.

Option 2: Run in an Online Compiler
1. Choose an online compiler (e.g., Repl.it, Ideone).
2. Create a new project and select Python.
3. Paste the code.
4. Click the "Run" button.

Option 3: Run in a Jupyter Notebook
1. Install Jupyter Notebook.
2. Create a new notebook and select Python.
3. Paste the code into a cell.
4. Click the "Run" button or press Shi
ft+Enter.
QSN3:?The purpose of the code?
ANS:
The purpose of the code is to implement two search algorithms:

Binary Search
Binary Search is used to find an element in a *sorted* list.

Linear Search
Linear Search is used to find an element in an *unsorted* or *sorted* list.

Both algorithms return the *index* of the target element if found, or *-1* if not found.

QNS4?:The time complexity, also tell the worst case of the binary search O(n), and print that numbers
ANS:
Time Complexity
- *Binary Search*: O(log n)
- *Linear Search*: O(n)

Worst-Case Scenario for Binary Search
Although Binary Search has a time complexity of O(log n), in the worst-case scenario, it can be O(n) when:

- The list is empty.
- The list has only one element.

However, for a list with 'n' elements, the worst-case time complexity of Binary Search remains O(log n).

Example Numbers for Binary Search
Suppose we have a sorted list of numbers: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

If we search for the number `5` using Binary Search:

1. The algorithm starts by checking the middle element (`5`).
2. Since `5` is the target element, the algorithm returns the index `4`..

In this example, Binary Search finds the target element in just one step, demonstrating its efficiency.



