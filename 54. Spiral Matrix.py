class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        elif len(matrix[0]) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix) == 2:
            result = matrix[0] + matrix[1][::-1]
            return result
        if len(matrix[0]) == 1:
            result = []
            for i in matrix:
                result.append(i[0])
            return result
        result = []
        m = len(matrix)  # numb of row
        n = len(matrix[0])  # numb of column
        result += matrix[0]
        result += [k[-1] for k in matrix[1:m - 1]]
        result += matrix[-1][::-1]
        result += [k[0] for k in matrix[1:m - 1]][::-1]
        matrix.pop(m - 1)
        matrix.pop(0)
        for k in matrix:
            k.pop(-1)
            k.pop(0)
        left_result = self.spiralOrder(matrix)
        result += left_result
        return result
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
