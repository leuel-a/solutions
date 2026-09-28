class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = [0 for _ in range(len(seq))]

        A = []
        B = []
        depthA = 0
        depthB = 0
        OPENING_BRACE = "("

        for i, char in enumerate(seq):
            if char == OPENING_BRACE:
                if depthA <= depthB:
                    depthA += 1
                    A.append((i, char))
                else:
                    depthB += 1
                    B.append((i, char))
            else:
                if A[-1][1] == OPENING_BRACE:
                    opening = A.pop()

                    aux = []
                    while A:
                        aux.append(A.pop())

                    A.append(opening)
                    A.append((i, char))

                    while aux:
                        A.append(aux.pop())

                    depthA -= 1
                else:
                    opening = B.pop()

                    aux = []
                    while B:
                        aux.append(B.pop())

                    B.append(opening)
                    B.append((i, char))

                    while aux:
                        B.append(aux.pop())

                    depthB -= 1
        for i, _ in B:
            answer[i] = 1
        return answer
