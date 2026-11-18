import function as func
import time

now = time.strftime("%d %b %Y %H:%M:%S")
print(now)

is_continue = True

while is_continue:
    user_prompt = input("Type add, show, edit, complete or exit : ")
    user_prompt = user_prompt.strip().lower()

    if user_prompt.startswith("add"):

        todo = user_prompt[4:] + "\n"
        todos = func.open_file()
        todos.append(todo)
        func.write_file(todos)

    elif user_prompt.startswith("show"):

        todos = func.open_file()
        for index, item in enumerate(todos):
            print(f"{index+1}.{item.strip("\n")}")

    elif user_prompt.startswith("edit"):  
        try:
            number = int(user_prompt[5:])
            if number -1 >= len(todos) or number - 1 < 0:
                raise IndexError
            new_todos = input("Enter a new todo : ") + "\n"
            todos = func.open_file()
            todos[number-1] = new_todos
            func.write_file(todos)
        except ValueError:
            print("please input number format")
            continue
        except IndexError:
            print("there's not todo with the number")

    elif user_prompt.startswith("complete"):
        try:
            number = int(user_prompt[9:])
            index = number-1
            todos = func.open_file()
            print(f"{todos[index].strip("\n")} removed from todos")
            todos.pop(index)
            func.write_file(todos)
        except IndexError:
            print("your todo is not found")
            exit()

    elif user_prompt.startswith("exit"):
        is_continue = False
    else:
        print("Not found")