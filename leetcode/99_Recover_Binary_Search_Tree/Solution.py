#!/usr/bin/python3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In-Place Solution -> O(n) Time Complexity + O(1) Space Complexity
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """Do not return anything, modify root in-place instead."""
        firstViolation: TreeNode | None = None
        secondViolation: TreeNode | None = None
        prevNode: TreeNode | None = None

        def sort(node: TreeNode | None):
            nonlocal prevNode, firstViolation, secondViolation
            if not node:
                return

            sort(node.left)
            if prevNode and prevNode.val > node.val:
                if not firstViolation:
                    firstViolation = prevNode
                secondViolation = node

            prevNode = node
            sort(node.right)

        sort(root)

        if firstViolation and secondViolation:
            firstViolation.val, secondViolation.val = secondViolation.val, firstViolation.val

# BRUTE FORCE APPROACH --> O(n) Space Complexity, O(2n + nlog(n)) Time Complexity
# class Solution:
#     def recoverTree(self, root: TreeNode | None) -> None:
#         """Do not return anything, modify root in-place instead."""
#         values = []
#
#         def inorderTraversal(node: TreeNode | None):
#             if not node:
#                 return
#
#             inorderTraversal(node.left)
#             values.append(node.val)
#             inorderTraversal(node.right)
#
#         inorderTraversal(root)
#         values.sort()
#
#         index = 0
#         def sort(node: TreeNode | None):
#             nonlocal index
#             if not node:
#                 return
#
#             sort(node.left)
#             if values[index] != node.val:
#                 node.val = values[index]
#             index = index + 1
#             sort(node.right)
#
#         sort(root)

