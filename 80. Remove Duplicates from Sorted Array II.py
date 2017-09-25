class Solution(object):
    def removeDuplicates(self, nums):
        alread_went = set()
        lenth = 0
        index = 0
        if len(nums) == 0:
            return 0
        while index < len(nums):
            if nums[index] in alread_went:
                index += 1
            else:
                if index + 1 < len(nums):
                    if nums[index + 1] == nums[index]:
                        alread_went.add(nums[index])
                        nums[lenth] = nums[index]
                        nums[lenth + 1] = nums[index + 1]
                        index += 2
                        lenth += 2
                    else:
                        alread_went.add(nums[index])
                        nums[lenth] = nums[index]
                        index += 1
                        lenth += 1
                else:
                    alread_went.add(nums[index])
                    nums[lenth] = nums[index]
                    lenth += 1
                    index += 1
        return lenth

        """
        :type nums: List[int]
        :rtype: int
        """