class Solution(object):
    def addBinary(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        a, b = list(a), list(b)
        add_numb = 0
        index = -1
        while index >= -len(a):
            pot = 0
            if index >= -len(b):
                pot = int(b[index])
            result = int(a[index]) + add_numb + pot
            add_numb = 0
            if result > 1:
                result = result - 2
                add_numb += 1
            a[index] = result
            index -= 1

        if add_numb == 1:
            a = [1] + a
        ret_result = ''
        for i in a:
            ret_result = ret_result + str(i)
        return ret_result

        """
        :type a: str
        :type b: str
        :rtype: str
        """
