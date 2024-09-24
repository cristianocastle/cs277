#Naithen Ramirez, cris padilla Lab 5, Group 12
def main_menu():
    pass

def read_file():
    file = open("tasklist.txt","r")
    task_list = []
    for line in file:
        task_objects = line.strip().split(",")
        if len(task_objects) == 3:
            desc, date, time = task_objects
            task = Task(desc,date,time)
            task_list.append(task)
    return task_list
def write_file(tasklist):
    pass

def get_date():
    pass

def get_time():
    pass

def main():
    test = read_file()
    print(test)

main()
