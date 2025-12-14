from typing import List
from node import Node

class Solution:
    def copyRandomList(self,  head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hM = {None: None}


        while curr:
            copy = Node(curr.val)
            hM[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hM[curr]
            copy.next = hM[curr.next]
            copy.random = hM[curr.random]
            curr = curr.next
        return hM[head]