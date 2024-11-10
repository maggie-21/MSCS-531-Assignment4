class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Inserts a value into the max-heap."""
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
        """Removes and returns the maximum value from the max-heap."""
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
        """Sorts elements by repeatedly extracting the max."""
        sorted_array = []
        while len(self.heap) > 0:
            sorted_array.insert(0, self.extract_max())
        return sorted_array


# Initialize the max-heap and insert elements
heap = MaxHeap()
for value in [50, 30, 40, 60]:
    heap.insert(value)

# Perform Heapsort
sorted_array = heap.heapsort()
print("Sorted Array:", sorted_array)  # Expected output: [30, 40, 50, 60]
