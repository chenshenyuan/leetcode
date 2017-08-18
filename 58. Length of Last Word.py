class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        index = -1
        while index > -len(s):
            if s[index] != ' ':
                index -= 1
            else:
                return (-1 - index)
        if index == -len(s):
            return len(s)
        return 0
        """
        :type s: str
        :rtype: int
        """
