tasks = []

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    print("\n--- Danh sách công việc ---")
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f"Đã hoàn thành: '{tasks[task_index - 1]['name']}'")
    else:
        print("Chỉ số không hợp lệ!")

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    complete_task(1)
    list_tasks()