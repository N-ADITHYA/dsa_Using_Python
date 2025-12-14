from node import Node


class SpecialLinkedList:
    def __init__(self):
        self.head = None

    def array_to_special_linkedlist(self, arr):
        if not arr:
            return self.head
        dA = [0] * len(arr)
        for i in range(len(arr)):
            dA[i] = Node(arr[i][0])

        for j in range(len(arr) - 1):
            dA[j].next = dA[j+1]

        for r in range(len(arr)):
            if arr[r][1] is None:
                dA[r].random = None
            else:
                dA[r].random = dA[arr[r][1]]
        self.head = dA[0]
        return self.head

    def print(self):
        curr = self.head
        while curr:
            if curr.next is None:
                print("Val is: ", curr.val, "Current pointer is: ", curr, "Next value is: ", curr.next, "Next values pointer: ", curr.next, "This values random pointer is: ", curr.random)
                break
            print("Val is: ", curr.val, "Current pointer is: ", curr, "Next value is: ", curr.next.val, "Next values pointer: ", curr.next, "This values random pointer is: ", curr.random)
            curr = curr.next



