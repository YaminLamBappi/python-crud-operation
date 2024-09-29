class ToDo:
    def __init__(self):
        self.task_list = []
        
    def view_task(self):
        if not self.task_list:
            print("\nthere is no task.")
        else:
            print("\nYour tasks are. \n")
        for index, task in enumerate(self.task_list):
            print(f'{index+1}: {task}')
            
    
    def add_task(self):
        task = str(input('Enter your task: '))
        self.task_list.append(task) 
        print("task added.")    

    def delete_task(self):
        self.view_task()
        index = int(input("which task you want to delete: "))
        
        if index<=0 or index>(len(self.task_list)):
            print("wrong task number to remove. try again")
        else:
            print(f'{self.task_list.pop(index-1)} removed from the list.')
        
    
    def interface(self):
        while True:
            
            print("\n1- View Task.\n2- Add Task.\n3- Remove task.")
            action = int(input("Enter your action: "))
            try:
                
                if action == 1:
                    self.view_task()
                elif action == 2:
                    self.add_task()
                elif action == 3:
                    self.delete_task()
                else:
                    print("invalid input. try again")
                    self.interface()
            except ValueError:
                print("invalid input.")
            
    
obj = ToDo()
obj.interface()