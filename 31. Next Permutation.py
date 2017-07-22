class Solution(object):
    def nextPermutation(self, nums):
        index_end = len(nums) - 1
        key = True
        while index_end > 0:
            if nums[index_end] <= nums[index_end - 1]:
                index_end -= 1
            else:  # nums[index_end]>=nums[index_end-1]:
                if index_end == len(nums) - 1:
                    nums[index_end - 1], nums[index_end] = nums[index_end], nums[index_end - 1]

                    key = False
                    break
                else:
                    find_index = len(nums) - 1
                    while find_index > index_end and nums[find_index] <= nums[index_end - 1]:
                        find_index -= 1
                    if find_index == index_end:
                        nums[index_end - 1], nums[index_end] = nums[index_end], nums[index_end - 1]
                        nums[index_end:] = sorted(nums[index_end:])
                        nums = nums[:index_end] + nums[index_end:]
                        key = False
                        break
                    else:
                        nums[index_end - 1], nums[find_index] = nums[find_index], nums[index_end - 1]
                        nums[index_end:] = sorted(nums[index_end:])

                        nums = nums[:index_end] + nums[index_end:]

                        key = False
                        break

        if key:
            nums.sort()

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
