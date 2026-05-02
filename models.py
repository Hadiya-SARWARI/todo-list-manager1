class Task:
    def __init__(self, title, priority="medium", completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not done"
        return f"{self.title} | Priority: {self.priority} | Status: {status}"

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }