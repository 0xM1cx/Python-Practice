class Queue:
    def __init__(self):
        self.queue =  []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    
    def display(self):
        print(self.queue)


q = Queue()


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()
print(q.dequeue())
q.display()
print(q.dequeue())
q.display()
q.enqueue(15)
q.display()


second = Queue()
second.enqueue(1)
