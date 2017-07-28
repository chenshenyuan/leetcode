def Is_valid(list1):
    for i in range(len(list1)):
        if list1[i] == '.':
            pass
        else:
            if i == len(list1) - 1:
                return True
            else:
                if list1[i] in list1[i + 1:]:
                    return False
    return True


def get_quear_tested(row_ind_list, col_ind_list, matrix_list2):
    result1 = []
    for i in row_ind_list:
        result1.append(matrix_list2[i])
    result2 = []
    for i in result1:
        for k in col_ind_list:
            result2.append(i[k])

    return Is_valid(result2)


class Solution(object):
    def isValidSudoku(self, board):
        for i in board:
            if not Is_valid(i):
                return False
        for i in range(len(board[0])):
            test_list = []
            for k in board:
                test_list.append(k[i])
            if not Is_valid(test_list):
                return False
        square_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in square_list:
            for k in square_list:
                test_result = get_quear_tested(i, k, board)
                if not test_result:
                    return False
        return True

        """
        :type board: List[List[str]]
        :rtype: bool
        """