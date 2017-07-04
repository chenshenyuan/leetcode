class Solution(object):
    def maxArea(self, height):
        beg_index = 0
        end_index = len(height)-1
        max_height = min(height[beg_index],height[end_index])
        max_numb = (end_index-beg_index)*max_height
        while beg_index<end_index and beg_index<len(height) and end_index >= 0:
            while height[beg_index]<=max_height and beg_index<end_index and beg_index<len(height) and end_index >= 0:
                beg_index+=1
            while height[end_index]<=max_height and beg_index<end_index and beg_index<len(height) and end_index >= 0:
                end_index-=1
            max_height = min(height[beg_index],height[end_index])
            max_numb = max(max_numb,max_height*(end_index-beg_index))

        return max_numb


list1 = [1,1]

wf = Solution()
print(wf.maxArea(list1))

















