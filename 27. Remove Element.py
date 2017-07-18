# second tricky question, but adapt to it

class Solution(object):
    def removeElement(self, nums, val):

        write_index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
