class Solution(object):
    def get_space(self, list1):
        level = min(list1[0], list1[-1])
        space1 = 0
        for k in range(1, len(list1) - 1):
            space1 += (level - list1[k])
        return space1

    def up_finding(self, list_input):
        beg_k = 0
        beg_height = list_input[beg_k]
        storages = 0
        for k in range(1, len(list_input)):
            if list_input[k] >= beg_height:
                beg_k = k
                beg_height = list_input[beg_k]
            else:
                storages += (beg_height - list_input[k])

        return storages

    def trap(self, height):
        if len(height) == 0:
            return 0

        max_level = max(height)
        if max_level == 0:
            return 0
        max_index = []
        spaces = 0
        for k in range(len(height)):
            if height[k] == max_level:
                max_index.append(k)
        space = self.up_finding(height[:(max_index[0] + 1)])
        spaces += space
        space = self.up_finding(height[max_index[-1]:][::-1])
        spaces += space
        if len(max_index) > 1:
            for k in range(1, len(max_index)):
                space = self.get_space(height[(max_index[k - 1]):(max_index[k] + 1)])
                spaces += space
        return spaces

        """
        :type height: List[int]
        :rtype: int
        """
