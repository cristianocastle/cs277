# naithen ramirez, cris padilla
# 11/21/24
# this program is a tasklist 

from check_input import get_int_range
from tasklist import Tasklist

def main_menu():
    print("1. Display all tasks")
    print("2. Display current task")
    print("3. Add new task")
    print("4. Mark current task complete")
    print("5. Postpone current task")
    print("6. Search tasks by date")
    print("7. Save and quit")
    return get_int_range("Enter your choice: ", 1, 7)

def get_date():
    """
    Prompts the user to enter a date and returns it in MM/DD/YYYY format.
    
    Returns:
        str: The date entered by the user in MM/DD/YYYY format.
    """
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter Day: ", 1, 31)
    year = get_int_range("Enter Year: ", 2000, 2100)
    
    return f"{month:02d}/{day:02d}/{year}"

def get_time():
    """
    Prompts the user to enter a time and returns it in HH:MM format.
    
    Returns:
        str: The time entered by the user in HH:MM format.
    """
    hour = get_int_range("Enter Hour: ", 0, 23)
    minute= get_int_range("Enter minute: ", 0 , 59)
    return f"{hour:02d}:{minute:02d}"

def main():
    tasklist = Tasklist()
    while True:
        print("\n-Tasklist-")
        print(f"You have {len(tasklist)} tasks")
        choice = main_menu()
        if choice == 1:
            print("\nTask to complete:")
            if len(tasklist) == 0:
                print("No tasks")
            else:
                for i, task in enumerate(tasklist):
                    print(f"{i+1}. {task}")
        elif choice == 2:
            print("\nCurrent task is:")
            current_task = tasklist.get_current_task()
            if current_task:
                print(current_task)
            else:
                print("All tasks are complete")
        elif choice == 3:
            description = input("Enter task description: ")
            print("Enter due date:")
            date = get_date()
            print("Enter time:")
            time = get_time()
            tasklist.add_task(description, date, time)
        elif choice == 4:
            print("\nMarking current task complete:")
            curent_task = tasklist.get_current_task()
            if curent_task:
                print(f"{curent_task}")
                tasklist.mark_complete()
                next_task = tasklist.get_current_task()
                if next_task:
                    print(f"Next current task is: \n{next_task}")
                else:
                    print("All tasks are complete")
            else:
                print("All tasks are complete")
        elif choice == 5:
            print("\nPostponing current task:")
            current_task = tasklist.get_current_task()
            if current_task:
                print (f"Postponing task: {current_task}")
                print("Enter new due date:")
                date = get_date()
                print("Enter new time:")
                time = get_time()
                tasklist.postpone_task(date, time)
            else:
                print("All tasks are complete")
        elif choice == 6:
            print("\nSearch by date:")
            search_date = get_date()
            print(f"\nTasks due on {search_date}:")
            matching_task = [task for task in tasklist if task.date == search_date]
            if matching_task:
                for i, task in enumerate(matching_task):
                    print(f"{i+1}. {task}")
            else:
                print("No matching tasks found for that date.")
        elif choice == 7:
            print("Saving list...")
            tasklist.save_file()
            break

if __name__ == "__main__":
    main()
