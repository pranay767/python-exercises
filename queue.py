class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data): #✅
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        self.rear.prev = new_node
        self.rear = new_node

    def dequeue(self):
        self.front = self.front.prev

    def peek(self):
        print(self.front.data)

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def is_empty(self):
        return self.front == None and self.rear == None

queue = Queue()

queue.enqueue(13)
queue.enqueue(23)
queue.enqueue(34)
queue.enqueue(2)
queue.enqueue(599)

queue.display()

queue.dequeue()

queue.display()
queue.peek()