from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a list (level order).
    Example: [1, 2, 3, None, 4]
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root
