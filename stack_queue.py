class DataStructure:
    def __init__(self):
        self.stack = []
        self.queue = []

    def stack_insert(self, item):
        self.stack.append(item)
        print(f"{item} pushed into the stack.")

    def stack_delete(self):
        if self.stack:
            item = self.stack.pop()
            print(f"{item} popped from the stack.")
        else:
            print("Stack is empty.")

    def stack_display(self):
        if self.stack:
            print("Current Stack: ", self.stack)
        else:
            print("Stack is empty.")

    def queue_insert(self, item):
        self.queue.append(item)
        print(f"{item} enqueued into the queue.")

    def queue_delete(self):
        if self.queue:
            item = self.queue.pop(0)
            print(f"{item} dequeued from the queue.")
        else:
            print("Queue is empty.")

    def queue_display(self):
        if self.queue:
            print("Current Queue: ", self.queue)
        else:
            print("Queue is empty.")

def stack_menu(ds):
    while True:
        print("\nStack Menu:")
        print("1. Insert into Stack")
        print("2. Delete from Stack")
        print("3. Display Stack")
        print("4. Quit to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter item to push into stack: "))
            ds.stack_insert(item)
        
        elif choice == '2':
            ds.stack_delete()
        
        elif choice == '3':
            ds.stack_display()
        
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        
        else:
            print("Invalid choice, please try again.")


def queue_menu(ds):
    while True:
        print("\nQueue Menu:")
        print("1. Insert into Queue")
        print("2. Delete from Queue")
        print("3. Display Queue")
        print("4. Quit to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter item to enqueue: "))
            ds.queue_insert(item)
        
        elif choice == '2':
            ds.queue_delete()
        
        elif choice == '3':
            ds.queue_display()
        
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        
        else:
            print("Invalid choice, please try again.")


def main_menu():
    ds = DataStructure()
    
    while True:
        print("\nMain Menu:")
        print("1. Stack Operations")
        print("2. Queue Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            stack_menu(ds)
        elif choice == '2':
            queue_menu(ds)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
