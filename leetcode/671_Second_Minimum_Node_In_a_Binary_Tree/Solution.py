import heapq
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        queue = deque()
        visited = set()
        heap = []
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.val not in visited:
                visited.add(node.val)
                heapq.heappush(heap, node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if len(heap) < 2:
            return -1

        print(heap)
        heapq.heappop(heap)
        return heapq.heappop(heap)
