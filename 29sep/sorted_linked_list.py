class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def add(self , data):
        # assuming the list is already sorted
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        if data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head #after object creation, youll use the obejct refernce right, thats why imgine self
        while current:
            if current.data == data:
                return
            if current.next is None:
                current.next = new_node
                return
            if data < current.next.data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next



sorted_ll = SortedLinkedList()

enumerate =