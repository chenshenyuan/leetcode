class Solution(object):
    def generateMatrix(self, n):
        result = [[0] * n for x in range(n)]
        l = 0
        r = n - 1
        filling_numb = 1
        while l < r:
            for i in range(l, r):
                result[l][i] = filling_numb
                filling_numb += 1
            for i in range(l, r):
                result[i][r] = filling_numb
                filling_numb += 1
            for i in range(r, l, -1):
                result[r][i] = filling_numb
                filling_numb += 1
            for i in range(r, l, -1):
                result[i][l] = filling_numb
                filling_numb += 1
            l += 1
            r -= 1
        if l == r:
            result[l][r] = filling_numb

        return result
        """
        :type n: int
        :rtype: List[List[int]]
        """
