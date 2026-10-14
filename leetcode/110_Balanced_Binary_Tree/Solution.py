# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check_height(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        left = self.check_height(node.left)
        if left == -1:
            return -1

        right = self.check_height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.check_height(root) != -1
