class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Wormhole Teleportation technique
        n = len(s)
        links = [-1] * n
        open_parenthesis = []

        for i, char in enumerate(s):
            if char == "(":
                open_parenthesis.append(i)
            elif char == ")":
                j = open_parenthesis.pop()

                links[i] = j
                links[j] = i

        result = []
        currentIndex = 0
        direction = 1

        while currentIndex < len(s):
            if s[currentIndex] in "()":
                direction *= -1
                currentIndex = links[currentIndex]
            else:
                result.append(s[currentIndex])
            currentIndex += direction
        return "".join(result)

# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         stack = []
#
#         for char in s:
#             if char == ")":
#                 current = []
#                 while stack and stack[-1] != "(":
#                     current.append(stack.pop())
#                 stack.pop()
#
#                 stack.extend(current)
#             else:
#                 stack.append(char)
#         return "".join(stack)
