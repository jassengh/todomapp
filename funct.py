def readings():
    with open("todos.txt", "r") as file:
        existing_todo = file.readlines()
    return existing_todo

def writings(existing_todo):
    with open("todos.txt", "w") as file:
        file.writelines(existing_todo)
