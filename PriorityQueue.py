from HeapSortWithMaxHeap import MaxHeap
from Task import Task
class PriorityQueue:
    def __init__(self):
        self.heap = MaxHeap()

    def insert_task(self, task):
        """Insert a new task into the priority queue."""
        self.heap.insert(task)

    def extract_highest_priority_task(self):
        """Extract the task with the highest priority."""
        return self.heap.extract_max()

    def increase_priority(self, task_id, new_priority):
        """Increase the priority of an existing task."""
        for i, task in enumerate(self.heap.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self.heap._heapify_up(i)
                return

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap.heap) == 0
