# too slow
class Solution(object):
    def isMatch(self, s, p):
        if len(s) == 0:
            if len(p) == 0:
                return True
            elif p[0] == '*':
                if self.isMatch('', p[1:]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            index_s, index_p = 0, 0
            while index_s < len(s) and index_p < len(p):
                if s[index_s] == p[index_p] or p[index_p] == '?':
                    index_s += 1
                    index_p += 1
                elif p[index_p] == "*":
                    index_p += 1
                    while index_p < len(p) and p[index_p] == "*":
                        index_p += 1
                    while index_s < len(s) and (not self.isMatch(s[index_s:], p[index_p:])):
                        index_s += 1
                    if self.isMatch(s[index_s:], p[index_p:]):
                        return True
                    else:
                        return False
                else:
                    return False
            if index_s >= len(s):
                if index_p >= len(p):
                    return True
                elif self.isMatch('', p[index_p:]):
                    return True
                else:
                    return False
            else:
                return False

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
