class Solution(object):
    def col_binary(self, col, target):
        l, r = 0, len(col) - 2
        if target >= col[r + 1]:
            return r + 1


class Solution(object):
    def col_binary(self, col, target):
        l, r = 0, len(col) - 2
        if target >= col[r + 1]:
            return r + 1
        elif target < col[l]:
            return -1
        while l <= r:
            mid = (l + r) // 2
            if col[mid] <= target and target < col[mid + 1]:
                return mid
            elif col[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def row_binary(self, row, target):
        l, r = 0, len(row) - 1
        if target < row[l] or target > row[r]:
            return -1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return mid
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False

        first_col = [matrix[x][0] for x in range(len(matrix))]
        row_index = self.col_binary(first_col, target)
        if row_index < 0:
            return False
        target_row = matrix[row_index]
        col_index = self.row_binary(target_row, target)
        if col_index < 0:
            return False
        else:
            return True

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """