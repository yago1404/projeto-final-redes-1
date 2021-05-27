from models.task import Task
from database import tasks


def createTask(title, description):
    new_task = Task(title, description)
    tasks.append(new_task)
    print('new task createde => ', tasks)
    return 'Task createde'

def deleteTask(title):
    index = 0
    for task in tasks:
        if task.title == title:
            tasks.pop(index)
            return "Task deletede"
        index += 1
    return "No task found"