#q2
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,num1):
        self.items.append(num1)

    def dequeue(self):
        if self.is_empty():
            print("bro u trying to pop a value from an empty queue :)")
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
    
    def show_Queue(self):   # lo 3ayez t print el arr bs :)
        print(self.items)


# ---------------- --------- -----------------
# ---------------- teasting ------------------
# ---------------- --------- -----------------


# q1 = Queue()
# q1.enqueue(1)
# q1.enqueue(2)
# q1.show_Queue()
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())
