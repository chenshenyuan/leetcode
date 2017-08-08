# the key concept is if it's better to choose one element, stop tem_result
class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]
        tem_result = nums[0]
        for i in nums[1:]:
            if i > tem_result + i:
                tem_result = i
            else:
                tem_result += i
            result = max(result, tem_result)
        return result

        """
        :type nums: List[int]
        :rtype: int
        """