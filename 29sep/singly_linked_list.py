class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#In single liked list, each node only knows whats after it, we cannot know what before, so we can travel only forward
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return #to terminate the function manually
        # code after this point will only be reached if the first new_node already there from second node onward
        current = self.head
        while current:
            if current.data == data:
                return
            # it reached this point means that current data was not equal to data
            if current.next is None:
                break
            current = current.next
        # if new_node.data != current.data: this chek is for anytime current.next yields None. it happens at end of list.
        # or when only single node there i.e. head node head.next is None, when there single node,
        # thats only the first and last node
        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def search(self,data):
        position = 0
        current = self.head
        while current:
            position += 1
            if current.data == data:
                return position
            current = current.next
        return None

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

    def remove(self, data):
        current = self.head
        

ll = SinglyLinkedList()

while True:
    num = int(input())
    if num == 0:
        break
    ll.add(num)

ll.display()

key = int(input("Search for "))
print("{} is found at {} place".format(key,ll.search(key))) #here its getting inputted as ll.search('20')