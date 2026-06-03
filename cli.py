import json

class Task:
    def __init__(self,name):
        self.title=name
        self.completed=False

    def to_dict(self):
        return {
            "title":self.title,
            "completed":self.completed
        }    
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,title):
        task=Task(title)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for i,task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{i}. {task.title} [{status}]")

    def mark_done(self,ind):
        self.tasks[ind].completed=True

    def del_task(self,ind):
        del self.tasks[ind]

    def save_tasks(self):
        data=[]
        for task in self.tasks:
            data.append(task.to_dict())
        with open("tasks.json","w")as file:
            json.dump(data,file,indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                for item in data:
                    task = Task(item["title"])
                    task.completed = item["completed"]
                    self.tasks.append(task)
        except FileNotFoundError:
            pass
manager=TaskManager()
manager.load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Done")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if choice==1:
        title=input("Task Title: ")
        manager.add_task(title)
        manager.save_tasks()

    elif choice==2:
        manager.list_tasks()

    elif choice==3:
        manager.list_tasks()
        try:
            num=int(input("Task number: "))
            manager.mark_done(num-1)
            manager.save_tasks()
            print("Task marked as completed.")
        except ValueError:
            print("Enter a valid number.")
        except IndexError:
            print("Task does not exist.")

    elif choice==4:
        manager.list_tasks()
        try:
            num = int(input("Task number: "))
            manager.del_task(num - 1)
            manager.save_tasks()
            print("Task deleted.")
        except ValueError:
            print("Enter a valid number.")
        except IndexError:
            print("Task does not exist.")
    elif choice ==5:
        manager.save_tasks()
        print("Tasks saved.")
        break
    else:
        print("Enter a valid choice!")