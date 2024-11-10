class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Task ID: {self.task_id}, Priority: {self.priority}"
