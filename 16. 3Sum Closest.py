class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_numb = float('inf')
        for i in range(len(nums)-2):
            L,R = i+1,len(nums)-1
            while L<R:
                sum_numb = nums[i]+ nums[L]+nums[R]
                if sum_numb == target:
                    return sum_numb
                pre_dis = abs(sum_numb - target)

                if pre_dis<=closest_numb:
                    result = sum_numb
                    closest_numb = pre_dis

                if sum_numb>target:
                    R-=1
                else:
                    L+=1
        return result

wf = Solution()
print(wf.threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33],0))
