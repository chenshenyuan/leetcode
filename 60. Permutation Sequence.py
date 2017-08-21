def find_fac(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


class Solution(object):
    def getPermutation(self, n, k):
        result = []
        opt_list = [x for x in range(1, n + 1)]
        k = k - 1
        while len(opt_list) > 1:
            fac = find_fac(len(opt_list) - 1)
            numb = k // (find_fac(len(opt_list) - 1))
            print(numb)
            result.append(opt_list[numb])
            opt_list = opt_list[:numb] + opt_list[numb + 1:]
            print(opt_list)
            k = k - numb * fac
            print(k)
        if len(opt_list) == 1:
            result.append(opt_list[0])
        result_str = ''
        for i in result:
            result_str += str(i)
        return result_str

        """
        :type n: int
        :type k: int
        :rtype: str
        """
