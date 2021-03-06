# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# made by Shenyuan and is accepted

class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        beg = 0;
        end = len(nums) - 1
        while beg < end:
            if sorted_nums[beg] + sorted_nums[end] == target:
                break
            elif sorted_nums[beg] + sorted_nums[end] > target:
                end = end - 1
            else:
                beg += 1
        ans1 = sorted_nums[beg]
        ans2 = sorted_nums[end]
        index1 = -1
        index2 = -1
        for i in range(len(nums)):
            if nums[i] == ans1 and index1 < 0:
                index1 = i
                continue
            if nums[i] == ans2 and index2 < 0:
                index2 = i

        return (index1, index2)

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

