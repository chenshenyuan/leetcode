class Solution(object):
    def permuteUnique(self, nums):
        if len(nums) <= 1:
            return [nums]
        elif len(nums) == 2:
            if nums[1] == nums[0]:
                return [nums]
            result = [nums]
            a = [nums[1], nums[0]]
            result.append(a)
            return result

        result = []
        already = []
        for i in range(len(nums)):
            first_numb = nums[i]
            if first_numb in already:
                continue
            else:
                already.append(first_numb)
            left_list = nums[0:i] + nums[i + 1:]
            result_of_left_list = self.permuteUnique(left_list)
            for k in result_of_left_list:
                if [first_numb] + k not in result:
                    result.append([first_numb] + k)
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
