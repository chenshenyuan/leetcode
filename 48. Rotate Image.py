class Solution(object):
    def rotate(self, matrix):
        down_limit = max_len = len(matrix[0]) - 1
        up_limit = 0
        while down_limit - 1 > up_limit + 1:

            # change four corner
            matrix[up_limit][up_limit], matrix[up_limit][down_limit], matrix[down_limit][up_limit], matrix[down_limit][
                down_limit] = matrix[down_limit][up_limit], matrix[up_limit][up_limit], matrix[down_limit][down_limit], \
                              matrix[up_limit][down_limit]
            a = up_limit + 1
            save_list = matrix[up_limit][up_limit + 1:down_limit]
            while a < down_limit:
                matrix[up_limit][max_len - a] = matrix[a][up_limit]
                matrix[a][up_limit] = matrix[down_limit][a]
                matrix[down_limit][a] = matrix[max_len - a][down_limit]
                matrix[max_len - a][down_limit] = save_list[down_limit - a - 1]
                a += 1
            down_limit -= 1
            up_limit += 1

        if down_limit - 1 == up_limit:
            matrix[up_limit][up_limit], matrix[up_limit][down_limit], matrix[down_limit][up_limit], matrix[down_limit][
                down_limit] = matrix[down_limit][up_limit], matrix[up_limit][up_limit], matrix[down_limit][down_limit], \
                              matrix[up_limit][down_limit]

        if down_limit - 1 == up_limit + 1:
            matrix[up_limit][up_limit], matrix[up_limit][down_limit], matrix[down_limit][up_limit], matrix[down_limit][
                down_limit] = matrix[down_limit][up_limit], matrix[up_limit][up_limit], matrix[down_limit][down_limit], \
                              matrix[up_limit][down_limit]
            mid_p = down_limit - 1
            matrix[up_limit][mid_p], matrix[down_limit][mid_p], matrix[mid_p][up_limit], matrix[mid_p][down_limit] = \
            matrix[mid_p][up_limit], matrix[mid_p][down_limit], matrix[down_limit][mid_p], matrix[up_limit][mid_p]

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
