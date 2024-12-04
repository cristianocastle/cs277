from task import Task
class Tasklist():
    def __init__(self):
        self.tasklist = []
        self.n = 0
        with open('tasklist.txt', 'r') as f:
            for line in f:
                desc, date, time = line.strip().split(',')
                self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()
    def add_task(self, desc, date, time):
        new_task = Task(desc, date, time)
        self.tasklist.append(new_task)
        self.tasklist.sort()
    
    def get_current_task(self):
        return self.tasklist[0]
    
    def mark_complete(self):
        if self.tasklist:
            return self.tasklist.pop(0)
        return None
    
    def postpone_task(self, date, time):
        if self.tasklist:
            current_task = self.tasklist.pop(0)
            new_task  = Task(current_task.desc, date, time)
            self.tasklist.append(new_task)
            self.tasklist.sort()
    def save_file(self):
        with open('tasklist.txt', 'w') as f:
            for task in self.tasklist:
                f.write(repr(task) + '\n')
    
    def __len__(self):
        return len(self.tasklist)
    
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < len(self.tasklist):
            task = self.tasklist[self.n]
            self.n += 1
            return task
        else:
            raise StopIteration
