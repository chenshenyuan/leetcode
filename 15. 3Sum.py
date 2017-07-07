# this one just killing me
# one rule: as simple as possible
# I have a lot of drafts using binary search and so on, which is useless in this case




class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return []

        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                test_result = nums[l]+nums[i]+nums[r]
                if test_result ==0:
                    result.append([nums[l],nums[i],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif test_result>0:
                    r -=1
                else:
                    l +=1

        return result