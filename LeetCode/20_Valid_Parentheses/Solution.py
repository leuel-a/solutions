class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_PARENTHESES, CLOSE_PARENTHESES = "(", ")"
        OPEN_BRACE, CLOSE_BRACE = "{", "}"
        OPEN_BRACKET, CLOSE_BRACKET = "[", "]"

        stack = []
        for char in s:
            if char in [OPEN_BRACE, OPEN_BRACKET, OPEN_PARENTHESES]:
                stack.append(char)
            else:
                if not stack:
                    stack.append(char)
                    continue

                if char == CLOSE_BRACE and stack[-1] == OPEN_BRACE:
                    stack.pop()
                elif char == CLOSE_BRACKET and stack[-1] == OPEN_BRACKET:
                    stack.pop()
                elif char == CLOSE_PARENTHESES and stack[-1] == OPEN_PARENTHESES:
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack) == 0
