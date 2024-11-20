# naithen ramirez, cris padilla
# 11/21/24
# this program is a tasklist 

from check_input import get_int_range

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
    pass

def get_time():
    pass