#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root: TreeNode | None = None

    def createNode(self, val: int) -> TreeNode:
        node = TreeNode(val, None, None)
        node.height = 1
        return node

    def rotateLeft(self, node: TreeNode) -> TreeNode:
        right_child = node.right

        node.right = right_child.left
        right_child.left = node

        node.height = AVLTree.updateHeight(node)
        right_child.height = AVLTree.updateHeight(right_child)

        return right_child

    def rotateRight(self, node: TreeNode) -> TreeNode:
        left_child = node.left

        node.left = left_child.right
        left_child.right = node

        node.height = AVLTree.updateHeight(node)
        left_child.height = AVLTree.updateHeight(left_child)

        return left_child


    def insert(self, val: int) -> None:
        if not self.root:
            self.root = self.createNode(val)
            return

        self.root = self.insertHelper(self.root, val)
        return

    @staticmethod
    def getHeight(node: TreeNode) -> int:
        if not node:
            return 0
        return node.height

    @staticmethod
    def updateHeight(node: TreeNode) -> int:
        return max(AVLTree.getHeight(node.left), AVLTree.getHeight(node.right)) + 1

    @staticmethod
    def getBalanceFactor(node: TreeNode) -> int:
        if not node:
            return 0
        return AVLTree.getHeight(node.left) - AVLTree.getHeight(node.right)

    def insertHelper(self, node: TreeNode | None, val: int) -> TreeNode:
        if not node:
            return self.createNode(val)

        if node.val > val:
            node.left = self.insertHelper(node.left, val)
        else:
            node.right = self.insertHelper(node.right, val)

        node.height = AVLTree.updateHeight(node)
        balance_factor = AVLTree.getBalanceFactor(node)

        if balance_factor > 1:
            if AVLTree.getBalanceFactor(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        elif balance_factor < -1:
            if AVLTree.getBalanceFactor(node.right) > 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        tree = AVLTree()

        for num in nums:
            tree.insert(num)

        return tree.root

