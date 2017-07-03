
# skip the 32 bit part since python usually hard to have this error
# max of 32bit number is 2147483647
# input or output larger than this will return 0



class Solution(object):
    def reverse(self, x):
        if abs(x) > (2147483647):
            return 0
        if x > 0:
            key1 = 1
        else:
            key1 = -1
            x = -x
        if x == 0:
            return 0

        a = str(x)
        result = ''
        for i in a:
            result = i + result
        if abs(int(result)) > (2147483647):
            return 0
        result = int(result) * key1

        return result



wf = Solution()
print(wf.reverse(1534236469))