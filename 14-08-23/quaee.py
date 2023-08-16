# class Queue:
#     def __init__(self,size):
#         self.items = []
#         self.size = size

#     def is_empty(self):
#         return len(self.items)==0
    
#     def is_full(self):
#         return len(self.items)==self.size

#     # pushing an elemnt to queue is called enqueing
#     def enqueue(self,item):
#         if self.is_full():
#             print("Queue is Full, try dequing some elements")
#         else:
#             self.items.append(item)

#     # deleting from the front is dequeing
#     def dequeue(self,count):
#         if self.is_empty():
#             return("Queue is empty")
#         else:
#             if count>=0:
#                 for i in range(count):
#                     quee =self.items.pop(i)
#                     print("queue:",Queue.display(self))
#                 return quee
        
#     def front(self):
#         if self.is_empty():
#             return("Queue is empty")
#         else:
#             return self.items[0]
        
#     def rear(self):
#         if self.is_empty():
#             return("Queue is empty")
#         else:
#             return self.items[-1]
        
#     def display(self):
#         return self.items
    
# q = Queue(10)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# q.enqueue(8)
# q.enqueue(9)
# q.enqueue(10)
# q.enqueue(11)

# print(q.display())
# q.dequeue(5)
# print(q.display())

# # suppose you are trying to enque more than the size of the queue,

# # so you need to return how many times you need to deque in order to enque one elemet.


class Print:
    def __init__(self):
        self.printingTasks = []

    def addPrintTaskToSchedule(self,printTask):
        if len(self.printingTasks)<5:
            self.printingTasks.append(printTask)
            print(f"Added task : {printTask}")
        else:
            print(f"Maximum task limit reched. Cannot add more taks. the tasks are: {self.printingTasks}")

    def printingTheTask(self):
        if len(self.printingTasks) == 0:
            print("No Tasks")
            return
        else:
            while self.printingTasks:
                printTask = self.printingTasks.pop(0)
                print(f"printing: {printTask}")


printScheduler = Print()

printScheduler.addPrintTaskToSchedule("Sravya's resume")
printScheduler.addPrintTaskToSchedule("Krishna's wiki page for telengana tourism")
printScheduler.addPrintTaskToSchedule("Bindu's Mahesh Babu poster")
printScheduler.addPrintTaskToSchedule("venky's allu arjun mp3 songs")
printScheduler.addPrintTaskToSchedule("vinod's python oop's concepts")
printScheduler.addPrintTaskToSchedule("praveen's daily stacks sheets")

printScheduler.printingTheTask()