

# test if exceed max numb limit
def test_max(input_numb):
    if input_numb>2147483647:
        return 2147483647
    elif input_numb< -2147483648:
        return -2147483648
    else:
        return input_numb


class Solution(object):
    def myAtoi(self, str):
        if len(str) == 0: # exclude empty str
            return 0
        result = ''
        key = 1
        sign_indic = 0
        empty_indic = 0
        for i in range(len(str)):
            if str[i] == " " and empty_indic == 0: #exclude blank ahead
                continue
            if str[i] == '-': # test '-'
                sign_indic = sign_indic + 1
                key = -1
                if sign_indic == 2: #exclude double +-
                    return 0
                else:
                    empty_indic += 1
                    continue
            elif str[i] == '+': #test '+'
                sign_indic = sign_indic + 1
                key = 1
                if sign_indic == 2: #exclude double +-
                    return 0
                else:
                    empty_indic += 1
                    continue
            else:
                try:
                    ele = int(str[i]) # try if it's convertable
                    if str[i] == ' ' and empty_indic > 0: # catch the middle blank space
                        if len(result) == 0:
                            return 0
                        result = int(result) * key
                        return test_max(result)
                    result = result + str[i]
                    empty_indic += 1
                except ValueError:
                    if len(result) == 0:
                        return 0
                    result = int(result) * key
                    return test_max(result)
        if len(result) == 0:
            return 0
        result = int(result) * key
        return test_max(result)

        """
        :type str: str
        :rtype: int
        """