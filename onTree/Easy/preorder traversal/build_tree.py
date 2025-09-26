from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildtree(values: List[Optional[int]]) -> Optional[TreeNode]:

    if not values or values[0] is None:
        return None
    i = 1
    root = TreeNode(values[0])
    queue = deque([root])

    while i < len(values) and queue:
        node = queue.popleft()
        if node is None:
            continue
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.left)
        i += 1
    return root
