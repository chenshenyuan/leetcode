
class Solution(object):
    def uniquePaths(self, m, n):
        board = [[-1]*m]*n
        for k in range(n):
            board[k][m-1]=1
        board[n-1] = [1]*m

        for i in range(n-2,-1,-1):
            for k in range(m-2,-1,-1):
                board[i][k]=board[i+1][k]+board[i][k+1]
        return board[0][0]