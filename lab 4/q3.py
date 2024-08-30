# q3:

class QueueOutOfRangeException(Exception):
    pass

class Queue_q3:
    _queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []
        Queue_q3._queues[name] = self

    def enqueue(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException(f"Queue '{self.name}' is full. you Can not add any other items.")
        else:
            self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print(f"Warning: bro u trying to pop a value from an empty queue '{self.name}' :).")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    @classmethod
    def get_queue_by_name(cls, name):
        return cls._queues.get(name)


# ---------------- --------- -----------------
# ---------------- teasting ------------------
# ---------------- --------- -----------------


# q1 = Queue_q3('Queue1', 3)
# q2 = Queue_q3('Queue2', 2)
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)

# print(q1.dequeue())
# print(q1.dequeue())  
# print(q1.dequeue())  
# print(q1.dequeue())  