class Solution(object):
    def setZeroes(self, matrix):
        row_set = set()
        col_set = set()
        for k in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[k][i] == 0:
                    row_set.add(k)
                    col_set.add(i)

        for w in row_set:
            for k in range(len(matrix[0])):
                matrix[w][k] = 0
        for w in col_set:
            for k in range(len(matrix)):
                matrix[k][w] = 0

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """