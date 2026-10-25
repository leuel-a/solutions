from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        self.visited = set()

        # at any point when exploring land if we encounter
        # a grid boundary its not a closed island

        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (
                    grid[i][j] == 0
                    and (i, j) not in self.visited
                    and self.checkIfIsland(grid, i, j)
                ):
                    islandCount += 1

        return islandCount

    def checkIfIsland(self, grid: list[list[int]], i: int, j: int) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        N = len(grid)
        M = len(grid[0])

        isIsland = True

        self.visited.add((i, j))
        queue = deque([(i, j)])
        while queue:
            row, col = queue.pop()

            for dx, dy in directions:
                nrow, ncol = row + dx, col + dy

                if (nrow < 0 or nrow >= N) or (ncol < 0 or ncol >= M):
                    isIsland = False
                    continue

                if (nrow, ncol) not in self.visited and grid[nrow][ncol] == 0:
                    self.visited.add((nrow, ncol))
                    queue.appendleft((nrow, ncol))

        return isIsland


