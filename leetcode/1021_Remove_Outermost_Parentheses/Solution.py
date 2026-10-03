class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count = 0
        close_count = 0

        start = -1
        result = []
        for i, char in enumerate(s):
            if char == "(":
                if start == -1:
                    start = i

                open_count += 1
            else:
                close_count += 1

            if open_count == close_count:
                for j in range(start + 1, i):
                    result.append(s[j])

                start = -1
                open_count = 0
                close_count = 0
        return "".join(result)
