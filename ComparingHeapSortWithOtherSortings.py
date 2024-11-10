import random
import time

# Heapsort
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        while index < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def heapsort(self):
        sorted_array = []
        while len(self.heap) > 0:
            sorted_array.insert(0, self.extract_max())
        return sorted_array

def heapsort(array):
    heap = MaxHeap()
    for num in array:
        heap.insert(num)
    return heap.heapsort()

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Helper function to time sorting algorithms
def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

# Generate test arrays
size = 1000
sorted_array = list(range(size))
reverse_sorted_array = sorted_array[::-1]
random_array = random.sample(range(size * 10), size)

# Test each sorting algorithm
print("Testing Heapsort:")
print("Sorted array:", time_sorting_algorithm(heapsort, sorted_array[:]))
print("Reverse-sorted array:", time_sorting_algorithm(heapsort, reverse_sorted_array[:]))
print("Random array:", time_sorting_algorithm(heapsort, random_array[:]))

print("\nTesting Quicksort:")
print("Sorted array:", time_sorting_algorithm(quicksort, sorted_array[:]))
print("Reverse-sorted array:", time_sorting_algorithm(quicksort, reverse_sorted_array[:]))
print("Random array:", time_sorting_algorithm(quicksort, random_array[:]))

print("\nTesting Merge Sort:")
print("Sorted array:", time_sorting_algorithm(mergesort, sorted_array[:]))
print("Reverse-sorted array:", time_sorting_algorithm(mergesort, reverse_sorted_array[:]))
print("Random array:", time_sorting_algorithm(mergesort, random_array[:]))
