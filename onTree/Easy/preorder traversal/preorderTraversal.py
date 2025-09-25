class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preorder(root):
            if root is None:
                return
            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return arr
