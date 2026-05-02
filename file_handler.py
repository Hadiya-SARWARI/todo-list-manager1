import csv
from models import Task


def save_tasks_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["title", "priority", "completed"])

        for task in tasks:
            writer.writerow([task.title, task.priority, task.completed])


def load_tasks_from_csv(filename="tasks.csv"):
    tasks = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task = Task(
                    row["title"],
                    row["priority"],
                    row["completed"] == "True"
                )
                tasks.append(task)

    except FileNotFoundError:
        pass

    return tasks


def save_summary_to_txt(tasks, filename="tasks_summary.txt"):
    with open(filename, "w") as file:
        file.write("TO-DO LIST SUMMARY\n")
        file.write("==================\n\n")

        if not tasks:
            file.write("No tasks available.\n")
        else:
            for number, task in enumerate(tasks, start=1):
                file.write(f"{number}. {task}\n")