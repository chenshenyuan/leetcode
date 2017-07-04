
# it's tricky since we could use string easily by replace the original int...
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x<10:
            return True
        x = str(x)
        beg_index = 0
        end_index = len(x)-1
        while beg_index<=end_index:
            if x[beg_index]==x[end_index]:
                beg_index+=1
                end_index+=1
                continue
            else:
                return False
        return True

        """
        :type x: int
        :rtype: bool
        """
wf = Solution()
print(wf.isPalindrome(1001))

