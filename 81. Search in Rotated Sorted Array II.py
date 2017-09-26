class Solution(object):
    def search(self, nums, target):
        l,r = 0,len(nums)-1

        while l<=r:
            mid_point = l+(r-l)//2
            if nums[mid_point]==target:
                return True
            while l< mid_point and nums[l]==nums[mid_point]:
                l+=1
            if nums[l]<= nums[mid_point]:
                if nums[l]<=target < nums[mid_point]:
                    r = mid_point-1
                else:
                    l = mid_point+1
            else: #nums[mid_point]<target
                if nums[mid_point]< target <=nums[r]:
                    l = mid_point+1
                else:
                    r = mid_point-1
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """