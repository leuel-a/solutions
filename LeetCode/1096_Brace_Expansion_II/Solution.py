from itertools import product


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0

        stack = []
        while i < len(expression):
            if expression[i].isalpha():
                j = i + 1
                while j < len(expression) and expression[j].isalpha():
                    j += 1

                operand = expression[i:j]
                i = j

                if not stack:
                    stack.append(operand)
                else:
                    if stack[-1] in ",{":
                        stack.append(operand)
                    else:
                        if stack[-1].isalpha():
                            aux = []
                            while stack and stack[-1].isalpha():
                                aux.append(stack.pop())

                            while aux:
                                stack.append(aux.pop() + operand)
                        else:
                            stack.extend(operand)

            elif expression[i] == "}":
                operand = []

                while stack and stack[-1] != "{":
                    top = stack.pop()
                    if top.isalpha():
                        operand.append(top)

                stack.pop()

                aux = []
                while stack and stack[-1].isalpha():
                    aux.append(stack.pop())

                if len(aux) != 0:
                    stack.extend([i + j for i, j in product(aux, operand)])
                else:
                    stack.extend(operand)
                i += 1
            else:
                stack.append(expression[i])
                i += 1
        return sorted(list(set(filter(lambda x: x != ",", stack))))

