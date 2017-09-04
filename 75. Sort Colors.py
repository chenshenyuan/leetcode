class Solution(object):
    def sortColors(self, nums):
        numbers = [0, 0, 0]
        for k in nums:
            numbers[k] += 1

        for k in range(len(nums)):
            if numbers[0] > 0:
                nums[k] = 0
                numbers[0] -= 1
            elif numbers[1] > 0:
                nums[k] = 1
                numbers[1] -= 1
            elif numbers[2] > 0:
                nums[k] = 2
                numbers[2] -= 1
            else:
                break

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """