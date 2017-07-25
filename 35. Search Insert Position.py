def binary_search(list1, target_numb):
    if target_numb < list1[0]:

        return 0
    elif target_numb > list1[-1]:
        return len(list1)
    else:
        l, r = 0, len(list1) - 1
        while l < r:
            if l + 1 == r:
                return r
            mid_point = (l + r) // 2

            if list1[mid_point] < target_numb:
                if list1[mid_point + 1] < target_numb:
                    l = mid_point + 1
                else:
                    return mid_point + 1
            else:  # midpoint > target
                if list1[mid_point - 1] > target_numb:
                    r = mid_point - 1
                else:
                    return mid_point


class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return binary_search(nums, target)

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """