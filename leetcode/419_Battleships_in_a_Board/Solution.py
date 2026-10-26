class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0

        N = len(board)
        M = len(board[0])

        for i in range(N):
            for j in range(M):
                if board[i][j] == 'X':
                    count += 1
                    self.discover(board, i, j)

        return count

    def discover(self, board: list[list[str]], i: int, j: int) -> None:
        N = len(board)
        M = len(board[0])

        board[i][j] = '.'
        if self.inBound(board, i, j + 1) and board[i][j + 1] == 'X':
            for k in range(j + 1, M):
                if board[i][k] == '.':
                    break
                board[i][k] = '.'
            return

        if self.inBound(board, i + 1, j) and board[i + 1][j] == 'X':
            for k in range(i + 1, N):
                if board[k][j] == '.':
                    break
                board[k][j] = '.'
            return

    def inBound(self, board: list[list[str]], i: int, j: int) -> bool:
        return (0 <= i < len(board)) and (0 <= j < len(board[0]))
