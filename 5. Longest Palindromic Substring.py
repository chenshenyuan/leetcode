
        # find the string with palindromic
def find_string(list1, num1, num2):
    while num1 >= 0 and num2 < len(list1):
        if list1[num1] == list1[num2]:
            re1 = num1
            re2 = num2
            num1 = num1 - 1
            num2 = num2 + 1
        else:
            break

    result = list1[re1:re2 + 1]
    return result

        # find the maximum repeat string since it's always be palindromic
def find_lenth(list1, start_index):
    lenth_aa = 0

    while start_index + lenth_aa < len(list1):
        if list1[start_index] == list1[start_index + lenth_aa]:
            lenth_aa = lenth_aa + 1
        else:
            break
    return lenth_aa - 1

        # find pattern, if it's repeat, keep find repeat
        # otherwise, find A b A type string
def find_mode(list1, start_index):
    while start_index + 1 < len(list1):
        if list1[start_index] == list1[start_index + 1]:
            lenth1 = find_lenth(list1, start_index)
            return [start_index, start_index + lenth1]

        elif start_index + 2 < len(list1):
            if list1[start_index] == list1[start_index + 2]:
                return [start_index, start_index + 2]
            else:
                start_index = start_index + 1

        else:
            start_index = start_index + 1


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        max_len = ''
        lenth1 = ''
        for i in range(len(s)):
            test_numb = find_mode(s, i)

            if test_numb != None:
                lenth1 = find_string(s, test_numb[0], test_numb[1])
            if len(max_len) < len(lenth1):
                max_len = lenth1

        if len(max_len) < 1:
            return s[0]

        return max_len

        """
        :type s: str
        :rtype: str
        """


x = 'babad'
wf = Solution()
print(wf.longestPalindrome(x))


