from collections import deque


class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        count = 0

        N = len(grid)
        M = len(grid[0])

        for i in range(N):
            for j in range(M):
                if grid[i][j] != 0 and self.checkIsland(grid, i, j, k):
                    count += 1

        return count

    def checkIsland(self, grid: list[list[int]], i: int, j: int, k: int) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        N = len(grid)
        M = len(grid[0])

        islandSum = grid[i][j]
        grid[i][j] = 0
        queue = deque([(i, j)])

        while queue:
            row, col = queue.pop()

            for dx, dy in directions:
                nrow = row + dx
                ncol = col + dy

                if (0 <= nrow < N and 0 <= ncol < M) and grid[nrow][ncol] != 0:
                    islandSum += grid[nrow][ncol]
                    grid[nrow][ncol] = 0

                    queue.appendleft((nrow, ncol))
        return islandSum % k == 0
