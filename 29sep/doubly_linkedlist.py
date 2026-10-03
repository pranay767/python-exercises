class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == data:
                return
            if current.next is None:
                break
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # def display_backward(self):
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #     while current:
    #         print(current.data,end=' -> ')
    #         current = current.prev
    #     print("None")

    def add(self, data):
        # assuming the list is already sorted
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        if data < self.head.data:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head  # after object creation, youll use the obejct refernce right, thats why imgine self
        while current:
            if current.data == data:
                return
            if current.next is None:
                current.next = new_node#make this make sense
                new_node.prev = current
                return
            if data < current.next.data:
                new_node.prev=current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

ll = DoublyLinkedList()

ll.append(13)
ll.append(20)
ll.append(25)
ll.add(22)
ll.display_forward()
# ll.display_backward()