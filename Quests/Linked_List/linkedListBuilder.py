class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.val, end="-->")
            curr = curr.next
        print("None")

    def ret(self):
        return self.head

