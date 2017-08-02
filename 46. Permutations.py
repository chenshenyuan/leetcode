class Solution(object):
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        if len(nums) == 2:
            result = [nums]
            a = [nums[1], nums[0]]
            result.append(a)
            return result
        result = []
        for i in range(len(nums)):
            first_numb = nums[i]
            left_list = nums[0:i] + nums[i + 1:]
            result_of_left_list = self.permute(left_list)
            for k in result_of_left_list:
                result.append([first_numb] + k)
        return result

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
