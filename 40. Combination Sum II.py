class Solution(object):
    def combinationSum2(self, candidates, target):
        if len(candidates) == 0:
            return []
        result = []

        if target in candidates:
            result.append([target])
        candidates = [i for i in candidates if i < target]
        if len(candidates) == 0:
            return result
        candidates.sort()

        for i in range(len(candidates)):
            new_target = target - candidates[i]

            if new_target < candidates[i]:
                continue
            tem_result = self.combinationSum2(candidates[i + 1:], new_target)
            if len(tem_result) > 0:
                for k in tem_result:
                    test = [candidates[i]] + k
                    if test not in result:
                        result.append([candidates[i]] + k)

        return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


