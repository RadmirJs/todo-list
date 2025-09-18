tasks = []


def show_tasks():
    if not tasks:
        print("Нет задач!")
    else:
        print("Ваши задачи:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(task):
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")


def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Задача '{removed}' удалена!")
    except IndexError:
        print("Такой задачи нет.")


while True:
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Введите задачу: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Введите номер задачи для удаления: "))
        delete_task(index)
    elif choice == "4":
        print("Выход...")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
