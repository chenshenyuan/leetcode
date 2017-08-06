class Solution(object):
    def groupAnagrams(self, strs):
        sorted_list = {}
        for sub_str in strs:
            test_str_list = tuple(sorted(sub_str))
            if not test_str_list in sorted_list:
                sorted_list[test_str_list] = []
            sorted_list[test_str_list].append(sub_str)
        return sorted_list.values()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
