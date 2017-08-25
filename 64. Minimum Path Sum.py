class Solution(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        board = []
        for k in range(n):
            row = []
            for i in range(m):
                row.append(0)
            board.append(row)

        board[n - 1][m - 1] = grid[n - 1][m - 1]

        for k in range(n - 2, -1, -1):
            board[k][m - 1] = board[k + 1][m - 1] + grid[k][m - 1]

        for k in range(m - 2, -1, -1):
            board[n - 1][k] = board[n - 1][k + 1] + grid[n - 1][k]

        for i in range(n - 2, -1, -1):
            for k in range(m - 2, -1, -1):
                board[i][k] = min(board[i + 1][k], board[i][k + 1]) + grid[i][k]

        return board[0][0]

        """
        :type grid: List[List[int]]
        :rtype: int
        """