from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        OPEN_PARENTHESES, CLOSE_PARENTHESES = "(", ")"
        result = []

        def backtrack(open: int, curr: List[str]):
            if len(curr) > (2 * n) or open < 0:
                return

            if len(curr) == (2 * n) and open == 0:
                result.append("".join(curr))
                return

            curr.append(OPEN_PARENTHESES)
            backtrack(open + 1, curr)
            curr.pop()

            curr.append(CLOSE_PARENTHESES)
            backtrack(open - 1, curr)
            curr.pop()

        backtrack(0, [])
        return result
