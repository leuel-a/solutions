# THIS WILL NOT WORK FOR NESTED BRACKETS TOO
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i = -1
        answer = []
        knowledgeDict = dict(knowledge)

        for j, char in enumerate(s):
            if char == "(":
                i = j
            elif char == ")":
                answer.append(knowledgeDict.get(s[i + 1: j], "?"))
                i = -1
            elif i < 0:
                answer.append(char)
        return "".join(answer)

# THIS WILL WORK FOR NESTED BRACKETS TOO
# class Solution:
#     def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
#         stack = []
#         knowledgeMap = dict(knowledge)
#
#         for val in s:
#             if val == ")":
#                 candidate = []
#                 while stack and stack[-1] != "(":
#                     candidate.append(stack.pop())
#                 stack.pop()  # remove (
#
#                 stack.extend(list(knowledgeMap.get("".join(candidate[::-1]), "?")))
#             else:
#                 stack.append(val)
#         return "".join(stack)
