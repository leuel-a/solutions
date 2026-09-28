class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        OPEN_PARENTHESES = "("

        stack: list[str] = []

        for char in s:
            if char == OPEN_PARENTHESES:
                stack.append(char)
            else:
                if stack[-1].isdigit():
                    acc = 0
                    while stack and stack[-1].isdigit():
                        acc += int(stack.pop())

                    stack.pop()
                    stack.append(str(2 * acc))
                else:
                    stack.pop()
                    stack.append("1")
        return sum(map(int, stack))
