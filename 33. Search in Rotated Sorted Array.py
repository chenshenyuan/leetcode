def binary_search(list1, target_numb):
    l, r = 0, len(list1) - 1

    while l <= r:

        mid_point = (l + r) // 2
        if list1[mid_point] == target_numb:
            return mid_point
        elif list1[mid_point] > target_numb:
            r = mid_point - 1
        else:
            l = mid_point + 1
    return -1

class Solution(object):
    def search(self, nums, target):
        if len(nums) <= 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        beg_numb = nums[0]
        end_numb = nums[-1]
        if target > end_numb and target < beg_numb:
            return -1
        elif target == end_numb or target == beg_numb:
            if target == end_numb:
                return len(nums) - 1
            else:
                return 0
        if end_numb > beg_numb:
            return binary_search(nums, target)

        mid_point = (len(nums) - 1) // 2
        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] > target:
            if nums[mid_point - 1] > nums[mid_point]:
                return -1
            if target < end_numb:
                if nums[mid_point] < end_numb:
                    return self.search(nums[:mid_point], target)
                result = self.search(nums[mid_point + 1:], target)
                if result != -1:
                    return result + mid_point + 1
                else:
                    return -1
            else:
                return self.search(nums[:mid_point], target)
        else:  # nums[mid_point]<target
            if nums[mid_point + 1] < nums[mid_point]:
                return -1
            if target > end_numb:
                if nums[mid_point] > end_numb:
                    result = self.search(nums[mid_point + 1:], target)
                    if result != -1:
                        return result + mid_point + 1
                    else:
                        return -1
                return self.search(nums[:mid_point], target)
            else:
                result = self.search(nums[mid_point + 1:], target)
                if result != -1:
                    return result + mid_point + 1
                else:
                    return -1

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """