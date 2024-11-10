from PriorityQueue import PriorityQueue
from Task import Task

# Create a priority queue
priority_queue = PriorityQueue()

# Insert tasks with different priorities
priority_queue.insert_task(Task("Task 1", 3))
priority_queue.insert_task(Task("Task 2", 1))
priority_queue.insert_task(Task("Task 3", 4))
priority_queue.insert_task(Task("Task 4", 2))

# Peek at the highest priority task
print("Highest Priority Task:", priority_queue.extract_highest_priority_task())  # Should be Task with priority 4

# Process remaining tasks by priority
print("Processing Remaining Tasks by Priority:")
while not priority_queue.is_empty():
    print(priority_queue.extract_highest_priority_task())
