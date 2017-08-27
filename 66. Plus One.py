class Solution(object):
    def plusOne(self, digits):
        add_numb = 1
        index = -1
        while add_numb == 1 and index >= -len(digits):
            sum_numb = digits[index] + add_numb
            add_numb -= 1
            if sum_numb >= 10:
                digits[index] = 0
                add_numb += 1
                index -= 1
            else:
                digits[index] = sum_numb
                break
        if add_numb == 1:
            digits = [1] + digits
        return digits

        """
        :type digits: List[int]
        :rtype: List[int]
        """
