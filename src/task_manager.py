from task import Task


class TaskManager:

    def __init__(self):
        self._tasks = list()

        self._not_started = 0
        self._in_progress = 0

    def add_task(self, name: str, desc: str = "", status: int = -1):
        if status not in [-1, 0, 1]:
            raise ValueError("Invalid status.")
        if len(name) == 0 or len(name) > 30:
            raise ValueError("Name must be between 1 and 30 characters long.")
        if len(desc) > 60:
            raise ValueError("Description must be below 60 characters long.")

        new_task = Task(name, desc, status)
        self._tasks.append(new_task)