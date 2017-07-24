def binary_search(list1, target_numb, left, right):
    l, r = left, right
    while l <= r:
        mid_point = (l + r) // 2
        if list1[mid_point] == target_numb:
            return [l, mid_point, r]
        elif list1[mid_point] > target_numb:
            r = mid_point - 1
        else:
            l = mid_point + 1
    return [-1]


class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) < 1:
            return [-1, -1]

        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        first_target = binary_search(nums, target, 0, len(nums) - 1)
        if len(first_target) == 1:
            return [-1, -1]

        min_index = r1 = l2 = max_index = first_target[1]
        l1 = first_target[0]
        r2 = first_target[2]
        key1 = True
        key2 = True
        while key1:
            result1 = binary_search(nums, target, l1, r1)
            if len(result1) == 1:
                key1 = False
            else:
                min_index = result1[1]
                l1 = result1[0]
                r1 = result1[1] - 1
        while key2:
            result1 = binary_search(nums, target, l2, r2)
            if len(result1) == 1:
                key2 = False
            else:
                max_index = result1[1]
                l2 = result1[1] + 1
                r2 = result1[2]

        return [min_index, max_index]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
