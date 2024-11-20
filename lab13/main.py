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
