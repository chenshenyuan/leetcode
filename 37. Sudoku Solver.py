# https://discuss.leetcode.com/topic/7475/accepted-python-solution

class Solution(object):
    def find_an_empty(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == '.':
                    return [x, y]
        return [-1, -1]

    def test_valid(self, x, y, value):
        key_row = False
        key_col = False
        key_sqr = False
        if value not in self.board[x]:
            key_row = True
        if value not in [self.board[i][y] for i in range(9)]:
            key_col = True
        sqr_list = []
        start_list = [0, 0]
        if x > 5:
            start_list[0] = 6
        elif x > 2:
            start_list[0] = 3
        if y > 5:
            start_list[1] = 6
        elif y > 2:
            start_list[1] = 3

        for k in range(start_list[0], start_list[0] + 3):
            for i in range(start_list[1], start_list[1] + 3):
                sqr_list.append(self.board[k][i])
        if value not in sqr_list:
            key_sqr = True

        if key_row and key_col and key_sqr:
            return True
        else:
            return False

    def solver(self):
        test_xy = self.find_an_empty()
        if test_xy == [-1, -1]:
            return True
        else:
            x = test_xy[0]
            y = test_xy[1]
            candidates = list('123456789')
            for candidate in candidates:
                if self.test_valid(x, y, candidate):
                    self.board[x][y] = candidate
                    if self.solver():
                        return True
                    self.board[x][y] = '.'
            return False

    def solveSudoku(self, board):
        self.board = board
        self.solver()

        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
