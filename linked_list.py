class Node():
    def __init__(self, data):
        self.value = data
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None

    def insert_at_start(self, x):
        newnode = Node(x)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insert_at_end(self, x):
        newnode = Node(x)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newnode

    def insert_before_item(self, x, item):
        newnode = Node(x)
        if x is None:
            return "Not valid"

        if self.head is None:
            self.head = newnode

        if self.head and self.head.value == item:
            newnode.next = self.head
            self.head = newnode
        else:
            n = self.head
            while n.next is not None:
                if n.next.value == item:
                    break
                n = n.next

            if n.next is None:
                return "not found"
            else:
                newnode.next = n.next
                n.next = newnode

    def transverse(self):
        n = self.head
        while n is not None:
            print(n.value)
            n = n.next

    def toArray(self):
        n = self.head
        arr = []

        while n is not None:
            arr.push(n.value)
            n = n.next

        return arr


mylist = Linked_list()
mylist.insert_at_start(6)
mylist.insert_at_end(5)
mylist.insert_at_start(9)
mylist.insert_at_start(50)
mylist.insert_at_end(2)
mylist.insert_before_item(7, 2)

print(mylist.transverse())
