class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#In single linked list, each node only knows whats after it, we cannot know what before, so we can travel only forward
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.top is not None:
            print(self.top.data)
        return None

    def pop(self):
        if not self.is_empty():
            top = self.top
            self.top = self.top.next
            return top.data
        return None

    def display(self):
        current = self.top
        print("Top\n ⬇")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.top is None


stack = Stack()

stack.push(10)
stack.push(10)
stack.push(1000000)
stack.display()
print(stack.pop())
# stack.display()
# stack.peek()
if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")
print(stack.__sizeof__())
