# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def lastRight(node: TreeNode) -> TreeNode:
            if not node.right:
                return node
            return lastRight(node.right)

        def convert(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return None

            left = convert(node.left)
            right = convert(node.right)

            if right:
                if left:
                    lastRight(left).right = right
                    node.right = left
            else:
                node.right = left
            node.left = None
            return node

        convert(root)
