class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True

        for i, numb in enumerate(nums):
            if numb != 0:
                pass
            else:
                if i == len(nums) - 1:
                    return True
                count = 1
                key = True
                while count < 10 and i - count >= 0:
                    if nums[i - count] > count:
                        key = False
                        break
                    else:
                        count += 1
                if key:
                    return False
        return True

        """
        :type nums: List[int]
        :rtype: bool
        """
