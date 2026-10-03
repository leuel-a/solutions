#!/usr/bin/python3


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set([])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def search(i: int, j: int, k: int) -> bool:
            if k == len(word) - 1:
                return True

            for dx, dy in directions:
                if (
                    in_bound(i + dx, j + dy)
                    and (i + dx, j + dy) not in visited
                    and board[i + dx][j + dy] == word[k + 1]
                ):
                    visited.add((i + dx, j + dy))
                    found = search(i + dx, j + dy, k + 1)
                    visited.remove((i + dx, j + dy))
                    if found:
                        return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue

                visited.add((i, j))
                found = search(i, j, 0)
                visited.clear()

                if found:
                    return True
        return False


def main():
    solution = Solution()
    print(
        solution.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )


if __name__ == "__main__":
    main()
