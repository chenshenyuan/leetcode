# Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500） and Ⅿ（1000）

def char_to_value(char1):
    list_cha = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    list_cha_mean = [1, 5, 10, 50, 100, 500, 1000]
    return list_cha_mean[list_cha.index(char1)]


class Solution(object):
    def romanToInt(self, s):
        sign_cha = ['I', 'X', 'C', 'M']
        if len(s) == 1:
            return char_to_value(s)
        if len(s) == 0:
            return 0
        print(s)
        # at least two digit
        index = 0
        base_char = s[index]
        base_value = char_to_value(base_char)
        test_char = s[index + 1]
        test_value = char_to_value(test_char)
        if base_value == test_value:  # like  III
            result = base_value
            index += 1
            while index < len(s):
                if s[index] == test_char:
                    result = result + test_value
                    index += 1
                else:
                    break

            if index == len(s):
                return result
            else:
                left_str = s[index:]
                left_value = self.romanToInt(left_str)
                result = result + left_value
                return result
        elif base_value == test_value * 5 or base_value == test_value * 10:
            result = base_value
            index += 1

            if index + 1 < len(s):
                if char_to_value(s[index + 1]) == base_value or char_to_value(s[index + 1]) == base_value / 2:
                    left_str = s[index:]
                    left_value = self.romanToInt(left_str)
                    result = result + left_value
                    return result
            while index < len(s):
                if s[index] == test_char:
                    result = result + test_value
                    index += 1
                else:
                    break

            if index == len(s):
                return result
            else:
                left_str = s[index:]
                left_value = self.romanToInt(left_str)
                result = result + left_value
                return result

        elif base_value * 5 == test_value or base_value * 10 == test_value:  # like IV or IX
            index += 1  # include test value
            result = test_value - base_value
            print('yes')
            index += 1  # try next element

            if index == len(s):  # end of s
                return result
            else:
                left_str = s[index:]
                left_value = self.romanToInt(left_str)
                result = result + left_value
                return result
        else:
            result = base_value
            index += 1
            left_str = s[index:]
            left_value = self.romanToInt(left_str)
            result = result + left_value
            return result

        """
        :type s: str
        :rtype: int
        """
