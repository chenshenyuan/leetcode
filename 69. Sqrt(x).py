def binary_search(x):
    l, r = 0, x
    while l <= r:
        mid_point = (l + r) // 2
        if mid_point * mid_point == x:
            return mid_point
        elif mid_point * mid_point > x:
            r = mid_point - 1
        else:
            l = mid_point + 1
    return r


class Solution(object):
    def mySqrt(self, x):
        return binary_search(x)

        """
        :type x: int
        :rtype: int
        """