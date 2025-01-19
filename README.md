Binary-and-Linear-Search
Overview
This project showcases the implementation of two fundamental searching algorithms in computer science: Binary Search and Linear Search. These algorithms are designed to efficiently locate a target value within an array or list, with each method demonstrating different approaches and time complexities.

Purpose of the Code
The primary goal of this project is to illustrate how to implement and utilize the Binary Search and Linear Search algorithms. By exploring these methods, you can gain a better understanding of the key principles behind data searching and algorithm efficiency.

How to Run the Program
Copy the code into your preferred IDE or text editor (e.g., VS Code, PyCharm, etc.).
Save the file with a .py extension (e.g., search_algorithms.py).
Run the script using Python:
python search_algorithms.py
Features
Binary Search
Description: Efficient searching algorithm that divides a sorted array into halves to locate the target value.
Requirements: The input array must be sorted.
Steps:
Compare the target value to the middle element of the array.
Narrow the search range to the left or right half based on the comparison.
Repeat until the value is found or the range is empty.
Linear Search
Description: A straightforward algorithm that iterates through each element of the array to find the target value.
Requirements: Works with both sorted and unsorted arrays.
Steps:
Traverse the array from the beginning.
Check each element against the target value.
Stop when the value is found or the end of the array is reached.
Time Complexity
Linear Search
Best Case: ( O(1) ) - If the target is the first element.
Worst Case: ( O(n) ) - If the target is the last element or not present in the array.
Binary Search
Best Case: ( O(1) ) - If the middle element matches the target.
Worst Case: ( O(\log n) ) - For sorted arrays, the search range is halved on each iteration.
Example Scenarios
Binary Search
Input:
My_Array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
My_Target = 15
Output:
Value 15 found at index 7
Linear Search
Input:
My_Numbers = [3, 7, 2, 9, 5]
Search_Value = 9
Output:
Value 9 is located at index 3
