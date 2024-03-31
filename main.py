### Задача про менеджер задач:

```python


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = "Не выполнено"

    def mark_as_done(self):
        self.status = "Выполнено"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                break

    def show_pending_tasks(self):
        for task in self.tasks:
            if task.status == "Не выполнено":
                print(f"{task.description}: {task.due_date} - {task.status}")


# Пример использования
manager = TaskManager()
manager.add_task("Купить продукты", "2023-04-10")
manager.add_task("Помыть машину", "2023-04-15")
manager.mark_task_done("Купить продукты")
manager.show_pending_tasks()