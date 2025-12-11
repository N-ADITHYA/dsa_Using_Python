from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[Node]) -> Optional[Node]:
        current = head

        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head