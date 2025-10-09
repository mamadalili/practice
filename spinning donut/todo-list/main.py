import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    print("\nMy first project:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['text']} {status}")
    print()

def main():
    tasks = load_tasks()
    while True:
        show_tasks(tasks)
        print("1) Add  2) Done  3) Delete  4) Quit")
        choice = input("Choose: ")
        if choice == "1":
            tasks.append({"text": input("Task: "), "done": False})
        elif choice == "2":
            i = int(input("Task number: ")) - 1
            tasks[i]["done"] = True
        elif choice == "3":
            i = int(input("Task number: ")) - 1
            tasks.pop(i)
        elif choice == "4":
            break
        save_tasks(tasks)

if __name__ == "__main__":
    main()
