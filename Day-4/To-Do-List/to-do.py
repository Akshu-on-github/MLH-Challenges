import os
import json


def add_task():
    task_ = []

    with open('tasks.json', 'r') as f:
        data = json.load(f)
        try:
            id  = int(list(data.keys())[-1]) + 1
            id = str(id)
        except:
            id = '1'

    title = str(input('Task title: '))
    description = str(input('Task description: '))
    date = str(input('Task date (dd-mm-yyyy): '))
    task_.append(title)
    task_.append(description)
    task_.append(date)
    data[id] = task_
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4)


def remove_task():
    with open('tasks.json', 'r') as f:
        data = json.load(f)

    for i in data.items():
        task_id = i[0]
        task_info = i[1]
        task_title = task_info[0]
        print(f'ID: {task_id}, Title: {task_title}')

    delete_id = str(input('[+] Enter ID to delete >> '))
    data.pop(delete_id)

    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4)
        
        
def show_tasks():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    for i in data.items():
        task_id = i[0]
        task_info = i[1]
        task_title = task_info[0]
        task_description = task_info[1]
        task_date = task_info[2]

        print(f'Task ID: {task_id}')
        print(f'    Task Title: {task_title}')
        print(f'    Task Description: {task_description}')
        print(f'    Task Date: {task_date}\n')
        
        
def app():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as f:
            f.write('{}')
    else:
        pass
    print('[!]Welcome to EddieHub To-Do-App!')
    try:
        mode = input('Chose your option number (eg:1): 1) Add a task  2) Show tasks  3) Delete a task >>')
        print('\n')
    except KeyboardInterrupt:
        pass
    if mode == '1':
        add_task()
    elif mode == '2':
        show_tasks()
    elif mode == '3':
        remove_task()
    else:
        pass


if __name__ == '__main__':
    app()
