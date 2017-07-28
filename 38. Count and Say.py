class Solution(object):
    def countAndSay(self, n):
        sequence = ['1', '11', '21', '1211', '111221']
        if n <= 5:
            return sequence[n - 1]
        beg_point = 5
        while beg_point < n:
            input_str = sequence[-1]
            index_beg = 1
            count = 1
            result = ''
            while index_beg < len(input_str):
                if input_str[index_beg - 1] == input_str[index_beg]:
                    count += 1
                    index_beg += 1
                else:
                    result = result + str(count) + input_str[index_beg - 1]
                    count = 1
                    index_beg += 1
            result = result + str(count) + input_str[index_beg - 1]

            sequence.append(result)
            beg_point += 1

        return sequence[-1]
        """
        :type n: int
        :rtype: str
        """
