class Solution:
    def minInsertions(self, s: str) -> int:
        min_changes = 0

        stack = []
        for char in s:
            if char == "(":
                if stack and stack[-1] == ")":
                    min_changes += 1
                    stack.pop() # first )
                    stack.pop() # then (
                stack.append(char)
            else:
                if not stack:
                    stack.append("(")
                    min_changes += 1
                    stack.append(char)
                else:
                    if stack[-1] == "(":
                        stack.append(char)
                    else:
                        stack.pop() # first )
                        stack.pop() # then (
        if stack and stack[-1] == ")":
            min_changes += 1
            stack.pop() # first )
            stack.pop() # then (
        return min_changes + (2 * len(stack))

