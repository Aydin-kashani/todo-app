
class to_do:
    """
    A simple to-do list manager that supports adding, showing,
    marking, deleting tasks, and exiting the program.
   """
   
    def __init__(self):
        # List of tasks; each task is a dictionary with 'title' and 'done'
        self.tasks = []
        
    def add_task(self):
        """
        Ask user for a task title and add it to the list.
        """
        title = input('Task title: ')
        # Validate empty input
        if title == False:
            print('The title cannot be empty!')    
        else:
            # Create task structure
            task = {'title': title, 'done': False}
            self.tasks.append(task)
            print(f"Task {task['title']} added ✅")
            
    def show_tasks(self):
        """
        Display all tasks with their index number and status.
        """
        i = 1
        # Loop through tasks with index
        for t in self.tasks:
            if t['done'] == True:
                status = '✅'
            else:
                status = '❌'
            print(f"{i}. {t['title']} {status}")
            i += 1
            
    def mark_as_done_delete(self):
        """
        Mark a task as done and optionally delete it.
        """
        if len(self.tasks) != 0:
            # Convert user input to task index
            num = int(input('The number of the completed task is: ')) - 1
            # Mark as done
            item_task = self.tasks[num]
            item_task['done'] = True
            print(f"Task {num + 1}. {item_task['title']} it’s done. ✅")
            print('Do you want to delete this task?')
            # Ask user whether to delete the completed task
            ask_delete = input('please insert Y or N: ')
            upper_ask = ask_delete.upper()
            if upper_ask == 'Y':
                del self.tasks[num]
                print('The task has been deleted.')
        else:
            print('The number is invalid.')
            
    def delete_task(self):
        """
        Delete a task by its number.
        """
        if len(self.tasks) != 0:
            num_delete = int(input('The task number you want to delete is: ')) - 1
            del self.tasks[num_delete]
            print('The task has been deleted.✅')
               
    def exit_program(self):
        """
        Print exit message and return False to stop main loop.
        """
        print('Exit. Goodbye!')
        return False
    
    
# ----------------------------------------------------------------------
# MAIN PROGRAM EXECUTION BLOCK
# ----------------------------------------------------------------------

start_program = True        
operation = to_do()


while start_program:
    print('\n📝 To-Do 📝')
    print('1) Add task')
    print('2) Show tasks')
    print('3) Mark as done')
    print('4) Delete task')
    print('5) Exit')
    
    # User menu selection
    choice_number = int(input('Choice: '))
    
    # Menu routing
    if choice_number == 1:
        operation.add_task()
        
    elif choice_number == 2:
        operation.show_tasks()
        
    elif choice_number == 3:
        operation.mark_as_done_delete()
        
    elif choice_number == 4:
        operation.delete_task()
        
    elif choice_number == 5:
        # Stop loop
        start_program = operation.exit_program()
        
    else:
        print('Invalid selection. Please enter a number between 1 and 5.')
        