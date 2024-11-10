# Heap Data Structures: Theoretical Analysis and Practical Applications

This project explores **heap data structures**, specifically focusing on **Heapsort** and **Priority Queue** applications. Heaps provide an efficient structure for sorting and priority management, widely used in areas like scheduling and data processing.

## Project Structure


- `HeapSortWithMaxHeap.py`: Contains the `MaxHeap` class and Heapsort implementation.
- `PriorityQueue.py`: Implements the `PriorityQueue` class with methods for managing tasks by priority.
- `Task.py`: Contains the `Task` class used in the priority queue for task management.
- `ComparingHeapSortWithOtherSortings.py`: Script for comparing Heapsort with other sorting algorithms (Quicksort and Merge Sort) on different input types, highlighting performance differences.
- `TestPriorityQueue.py`: Script for testing the priority queue implementation.
- `README.md`: This documentation file.
- `[MSCS-532]Assignment4.pdf`: PDF containing assignment details.

## Instructions for Running the Code

### 1. Heapsort
To test Heapsort, run the `HeapSortWithMaxHeap.py` script:
```
python3 HeapSortWithMaxHeap.py
```
### 3. Sorting Comparison
To compare Heapsort, Quicksort, and Merge Sort, run the `comparing_sorts.py` script:
```
python3 ComparingHeapSortWithOtherSortings.py
```
### 2. Priority Queue
To test the priority queue with task scheduler run the `TestPriorityQueue.py` script:
```
python3 TestPriorityQueue.py
```

## Summary of Findings

1. **Heapsort**: Consistent **O(n log n)** performance across all input types, though slightly slower than Quicksort due to higher constant factors.
2. **Quicksort**: Fastest in practice for random data, but with potential **O(n²)** worst-case complexity, mitigated here by pivot selection.
3. **Merge Sort**: Consistent **O(n log n)** performance and stable across inputs, though with an **O(n)** space complexity.

The priority queue implementation demonstrates effective task management by priority, showing heaps' versatility in sorting and scheduling applications.

## Algorithm Complexity Comparison

| **Algorithm** | **Best Case** | **Average Case** | **Worst Case** | **Space Complexity** |
|---------------|---------------|------------------|----------------|----------------------|
| Heapsort      | O(n log n)    | O(n log n)       | O(n log n)     | O(1)                 |
| Quicksort     | O(n log n)    | O(n log n)       | O(n²)          | O(log n)             |
| Merge Sort    | O(n log n)    | O(n log n)       | O(n log n)     | O(n)                 |
