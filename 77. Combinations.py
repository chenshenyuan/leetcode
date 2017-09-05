class Solution(object):
    def sub_combine(self, beg, end, numb_k):
        result = []
        if numb_k == 1:
            for w in range(beg, end + 1):
                result.append([w])
        else:
            for i in range(beg, end - numb_k + 2):
                sub_result = self.sub_combine(i + 1, end, numb_k - 1)
                for w in sub_result:
                    result.append([i] + w)
        return result

    def combine(self, n, k):
        result_list = self.sub_combine(1, n, k)
        return result_list

        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """