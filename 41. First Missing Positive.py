class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        rank_list = []
        for num in nums:
            if num > 0:
                if num < len(rank_list):
                    rank_list[num - 1] = num
                else:
                    rank_list = rank_list + [0] * (num - len(rank_list))
                    rank_list[num - 1] = num

        for k in range(len(rank_list)):
            if rank_list[k] == 0:
                return k + 1
        return len(rank_list) + 1
        """
        :type nums: List[int]
        :rtype: int
        """
