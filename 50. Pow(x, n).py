class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        memoization_dict = {0: 0}
        key = 1
        if n < 0:
            key = -1
            n = -n
        memoization_dict[1] = x
        result = 1
        count = 0
        while count < n:
            if n - count in memoization_dict.keys():
                result = result * memoization_dict[n - count]
                count = n
            elif n - count > max(memoization_dict.keys()):
                numb = max(memoization_dict.keys())
                result = result * memoization_dict[numb]
                count = count + numb
                memoization_dict[count] = result
            else:
                numb = max([i for i in memoization_dict.keys() if i < n - count])
                result = result * memoization_dict[numb]
                count = count + numb
                memoization_dict[count] = result
        if key < 0:
            return 1 / result
        else:
            return result

        """
        :type x: float
        :type n: int
        :rtype: float
        """
