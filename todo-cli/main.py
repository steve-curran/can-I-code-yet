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
# Add Tests
# Add pipeline to run tests using github actions

def print_welcome_message(): 
    indent = '\t' * 5
    print('-' * 50 + ' TODO CLI ' + '-' * 50)
    print(indent + 'Welcome to your todo list!')
    print(indent + ' ' * 50)
    print(indent + 'Type "Add" to Add a task')
    print(indent + 'Type "Show" to Show all tasks')
    print(indent + 'Type "Remove" to Remove a task')
    print(indent + 'Type "Complete" to complete a task')
    print(indent + 'Type "Exit" to end the program')
    print(indent + ' ' * 50)

def show_all_items():
    print('Here are all of your tasks:')
    for task in todo_list:
        print("- " , task)

def add():
    task_name = input('What task would you like to add? ')
    task_status = "incomplete"
    task = {
         "name" : task_name ,
         "status" : task_status
    }
    
    todo_list.append(task)

def remove():
    task_name = input('Enter the name of the task you would like to remove!')
    for task in todo_list :
         if task["name"] == task_name :
              todo_list.remove(task)
              return 

    print("It's not in the list.")
        
def complete():
    task_name = input('What task have you completed?')
    
    for task in todo_list:
        if task["name"] == task_name:
             task["status"] = "complete"
             print(f'Task "{task_name}" marked as complete.')
             return  
    
    print(f'Task"{task_name}" not found in the to-do list.')

            
def main_menu():
    command = input('What would you like to do? ')
    if command == 'Add': 
        add()

    if command == "Remove":
        remove()

    if command == "Complete":
        complete()

    if command == 'Exit':
        exit()
    
    show_all_items()
    main_menu()
    



def main(): 
    print_welcome_message()
    main_menu()


   



main()