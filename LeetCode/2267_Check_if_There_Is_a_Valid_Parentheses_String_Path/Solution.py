class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        OPENING_BRACE = "("

        if grid[0][0] != OPENING_BRACE:
            return False

        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                curr = grid[i][j]
                if i - 1 >= 0 and dp[i - 1][j] != 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

                if j - 1 >= 0 and dp[i][j - 1] != 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])

                if dp[i][j] == float('inf'):
                    dp[i][j] = 0

                if curr == OPENING_BRACE:
                    dp[i][j] += 1
                else:
                    dp[i][j] -= 1
        return dp[m - 1][n - 1] == 0

# Pruned Brute Force
# class Solution:
#     def hasValidPath(self, grid: list[list[str]]) -> bool:
#         OPEN_PARENTHESES = "("
#
#         def inBound(i: int, j: int) -> bool:
#             return 0 <= i < len(grid) and 0 <= j < len(grid[0])
#
#         directions = [(1, 0), (0, 1)]
#
#         def checkIfVPSExists(i: int, j: int, curr: int):
#             if grid[i][j] == OPEN_PARENTHESES:
#                 curr += 1
#             else:
#                 if curr > 0:
#                     curr -= 1
#                 else:
#                     return False
#
#             if i == (len(grid) - 1) and j == (len(grid[0]) - 1):
#                 return curr == 0
#
#             for dx, dy in directions:
#                 if inBound(i + dx, j + dy):
#                     if checkIfVPSExists(i + dx, j + dy, curr):
#                         return True
#             return False
#
#         return checkIfVPSExists(0, 0, 0)


# Brute Force Approach
# class Solution:
#     def hasValidPath(self, grid: list[list[str]]) -> bool:
#         OPENING_BRACE = "("
#         CLOSING_BRACE = ")"
#         stack = [grid[0][0]]
#         directions = [(1, 0),(0, 1)]
#
#         def inBound(row: int, col: int) -> bool:
#             return 0 <= row < len(grid) and 0 <= col < len(grid[0])
#
#         def checkIfVPSValid(candidate: str) -> bool:
#             path = []
#             for char in candidate:
#                 if char == OPENING_BRACE:
#                     path.append(OPENING_BRACE)
#                 else:
#                     if path and path[-1] == OPENING_BRACE:
#                         path.pop()
#                     else:
#                         path.append(CLOSING_BRACE)
#             return len(path) == 0
#
#         def checkIfVPSExists(row: int, col: int) -> bool:
#             if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
#                 return checkIfVPSValid("".join(stack))
#
#             for dx, dy in directions:
#                 if inBound(row + dx, col + dy):
#                     stack.append(grid[row + dx][col + dy])
#                     if checkIfVPSExists(row + dx, col + dy):
#                         return True
#                     stack.pop()
#             return False
#
#         return checkIfVPSExists(0, 0)
