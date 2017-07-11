class Solution(object):
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-3):
            if i-1>=0 and nums[i-1]==nums[i]:
                pass
            else:
                local_target = target - nums[i]
                for k in range(i+1,len(nums)-2):
                    if nums[k-1]==nums[k] and k-1 !=i:
                        pass
                    else:
                        local_target2 = local_target - nums[k]
                        l,r = k+1,len(nums)-1
                        temp_result = []
                        while l<r:
                            if nums[l]+nums[r]==local_target2:
                                temp_result.append([nums[k],nums[l],nums[r]])
                                while l+1<r and nums[l+1]==nums[l]:
                                    l+=1
                                while l<r-1 and nums[r-1]==nums[r]:
                                    r-=1
                                l+=1
                                r-=1
                            elif nums[l]+nums[r]<local_target2:
                                l+=1
                            else:
                                r-=1
                        if len(temp_result)>0:
                            for m in temp_result:
                                result.append([nums[i]]+m)
        return result