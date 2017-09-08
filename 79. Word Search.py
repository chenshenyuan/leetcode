class Solution(object):
    def search_word(self,board1,index_i,index_k,str1):
        if len(str1)==0:
            return True
        if index_i+1<len(board1) and board1[index_i+1][index_k]!='0' and board1[index_i+1][index_k]==str1[0]:
            board1[index_i + 1][index_k] = '0'
            if self.search_word(board1,index_i+1,index_k,str1[1:]):
                return True
            else:
                board1[index_i + 1][index_k] = str1[0]
        if index_i-1>=0 and board1[index_i-1][index_k]!='0' and board1[index_i-1][index_k]==str1[0]:
            board1[index_i - 1][index_k] = '0'
            if self.search_word(board1,index_i-1,index_k,str1[1:]):
                return True
            else:
                board1[index_i - 1][index_k] = str1[0]
        if index_k+1<len(board1[0]) and board1[index_i][index_k+1]!='0' and board1[index_i][index_k+1]==str1[0]:
            board1[index_i][index_k+1] = '0'
            if self.search_word(board1,index_i,index_k+1,str1[1:]):
                return True
            else:
                board1[index_i][index_k + 1] = str1[0]
        if index_k-1>=0 and board1[index_i][index_k-1]!='0' and board1[index_i][index_k-1]==str1[0]:
            board1[index_i][index_k-1] = '0'
            if self.search_word(board1,index_i,index_k-1,str1[1:]):
                return True
            else:
                board1[index_i][index_k - 1] = str1[0]
        return False

    def exist(self, board, word):
        if not board:
            return False
        if len(board)==1:
            if word in board:
                return True

        tem_board = []
        for w in board:
            print(list(w))
            tem_board.append(list(w))
        board = tem_board
        beg_char = word[0]

        for i in range(len(board)):
            for k in range (len(board[0])):
                if board[i][k] == word:
                    return True
                elif board[i][k]==beg_char:
                    tem_board = list(board)
                    tem_board[i][k]='0'
                    if self.search_word(tem_board,i,k,word[1:]):
                        return True
                    else:
                        tem_board[i][k] = beg_char
        return False





        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """