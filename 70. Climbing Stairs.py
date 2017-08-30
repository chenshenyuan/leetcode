class Solution(object):
    def climbStairs(self, n):
        list_ans = [0, 1, 2]
        index = len(list_ans)
        while index <= n:
            list_ans.append(list_ans[index - 1] + list_ans[index - 2])
            index += 1
        return list_ans[n]

        """
        :type n: int
        :rtype: int
        """
