from models import Task


# ✅ Decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Action: {func.__name__} is being executed")
        return func(*args, **kwargs)
    return wrapper


class ToDoManager:
    def __init__(self):
        self.tasks = []

    @log_action
    def add_task(self, title, priority="medium"):
        task = Task(title, priority)
        self.tasks.append(task)

    @log_action
    def delete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for number, task in enumerate(self.tasks, start=1):
                print(f"{number}. {task}")

    @log_action
    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_completed()
                return True
        return False

    def get_tasks_by_priority(self, priority):
        return list(filter(lambda task: task.priority == priority, self.tasks))