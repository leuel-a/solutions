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
