from typing import List


# Top Down DP Approach
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        self.s = s
        self.memo = [[-1] * n for _ in range(n)]

        return self.isValidString(0, 0) == 1

    def isValidString(self, index: int, open_count: int) -> int:
        if index == len(self.s):
            return open_count == 0

        if self.memo[index][open_count] != -1:
            return self.memo[index][open_count]

        isValid = False
        if self.s[index] == "*":
            isValid |= self.isValidString(index + 1, open_count + 1)

            if open_count > 0:
                isValid |= self.isValidString(index + 1, open_count - 1)

            isValid |= self.isValidString(index + 1, open_count)
        else:
            if self.s[index] == "(":
                isValid |= self.isValidString(index + 1, open_count + 1)
            elif open_count > 0:
                isValid |= self.isValidString(index + 1, open_count - 1)

        self.memo[index][open_count] = 1 if isValid else 0
        return self.memo[index][open_count]


# Bottom Up DP Approach
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         n = len(s)
#         dp = [[False] * (n + 1) for _ in range(n + 1)]
#
#         dp[n][0] = True
#
#         for i in range(n - 1, -1, -1):
#             for openBracket in range(n):
#                 isValid = False
#
#                 if s[i] == "*":
#                     if openBracket < n:
#                         isValid |= dp[i + 1][openBracket + 1]
#
#                     if openBracket > 0:
#                         isValid |= dp[i + 1][openBracket - 1]
#
#                     isValid |= dp[i + 1][openBracket]
#                 else:
#                     if s[i] == "(":
#                         isValid |= dp[i + 1][openBracket + 1]
#                     elif openBracket > 0:
#                         isValid |= dp[i + 1][openBracket - 1]
#
#                 dp[i][openBracket] = isValid
#
#         return dp[0][0]
