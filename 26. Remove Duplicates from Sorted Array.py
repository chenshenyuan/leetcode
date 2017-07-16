# this question is super tricky
# it's require the first unique number of element be unique
# so for [1,2,4,4,4,5,6,7], nums should be [1,2,4,5,6,7,6,7], last two elements keep unchanged


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)

        unique_numb = 1
        index_numb = 1
        while index_numb < len(nums):
            if nums[index_numb - 1] != nums[index_numb]:
                nums[unique_numb] = nums[index_numb]
                unique_numb += 1
            index_numb += 1

        return unique_numb

        """
        :type nums: List[int]
        :rtype: int
        """
