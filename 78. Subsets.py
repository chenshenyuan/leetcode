class Solution(object):
    def subset_choice(self,numb_list,need_numb):
        result_list = []
        if need_numb==0:
            return [result_list]
        elif need_numb==len(numb_list):
            return  [numb_list]
        elif need_numb==1:
            for k in numb_list:
                result_list.append([k])
            return result_list
        else:
            for k in range(len(numb_list)-need_numb+1):
                sub_set = self.subset_choice(numb_list[k+1:],need_numb-1)
                for w in sub_set:
                    result_list.append([numb_list[k]]+w)
            return result_list
    def subsets(self, nums):
        result_list = []
        need_numb = len(nums)
        while need_numb>=0:
            sub_set = self.subset_choice(nums,need_numb)
            for w in sub_set:
                result_list.append(w)
            need_numb-=1
        return result_list
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """