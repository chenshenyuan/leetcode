class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for k in range(n):
            for i in range(m):
                if obstacleGrid[k][i]==1:
                    obstacleGrid[k][i] = -1

        for k in range(n-1,-1,-1):
            if obstacleGrid[k][m - 1]==0:
                obstacleGrid[k][m - 1] = 1
            else:
                break

        for k in range(m-1,-1,-1):
            if obstacleGrid[n-1][k]!=-1:
                obstacleGrid[n-1][k] = 1
            else:
                break

        for i in range(n - 2, -1, -1):
            for k in range(m - 2, -1, -1):
                number1,number2 = 0,0
                if obstacleGrid[i + 1][k] != -1:
                    number1 = obstacleGrid[i + 1][k]
                if obstacleGrid[i][k + 1] != -1:
                    number2 = obstacleGrid[i][k + 1]
                if obstacleGrid[i][k] != -1:
                    obstacleGrid[i][k] = number1 + number2
        if obstacleGrid[0][0]==-1:
            return 0
        return obstacleGrid[0][0]
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """