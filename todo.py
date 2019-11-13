# keep track of todos using a list
todo_list = []
# i need to print my todos
def print_todos():
    for todo in todo_list:
        print(todo)
# i need a way to add todos
def add_todo(todo):
    todo_list.append(todo)

# print(todo_list)
add_todo("feed the cat")
# print(todo_list)
# i need to be able to delete todos
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no todo at that index.")
# delete_todo(0)
print_todos()


# show user main menu after every command

