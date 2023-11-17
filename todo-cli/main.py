todo_list = [] 


# Add a task to the list
# Show all tasks
# Remove task from list
# OBJECTS - Dictionary
# Mark task as complete
# CLASSES - Methods, properties 
# Add description to a task
# Add a project to a task
# Show all tasks for a project
# Add a due date to a task
# LOOPS
# Sort tasks by due date
# Add a priority to a task
# Types

def print_welcome_message(): 
    indent = '\t' * 5
    print('-' * 50 + ' TODO CLI ' + '-' * 50)
    print(indent + 'Welcome to your todo list!')
    print(indent + ' ' * 50)
    print(indent + 'Type "Add" to Add a task')
    print(indent + 'Type "Show" to Show all tasks')
    print(indent + 'Type "Remove" to Remove a task')
    print(indent + 'Type "Exit" to end the program')
    print(indent + ' ' * 50)

def show_all_items():
    print('Here are all of your tasks:')
    for task in todo_list:
        print("- " + task)

def add():
    task = input('What task would you like to add? ')
    todo_list.append(task)

def main_menu():
    command = input('What would you like to do? ')
    if command == 'Add': 
        add()

    if command == 'Exit':
        exit()
    
    show_all_items()
    main_menu()
    



def main(): 
    print_welcome_message()
    main_menu()


   



main()