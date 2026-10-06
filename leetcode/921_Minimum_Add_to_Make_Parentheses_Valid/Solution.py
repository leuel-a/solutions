class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_changes = 0
        open_brackets = 0

        for i, char in enumerate(s):
            if char == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_changes += 1

        return min_changes + open_brackets
