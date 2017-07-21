class Solution(object):
    def divide(self, dividend, divisor):
        key1, key2 = 1, 1
        if dividend < 0:
            key1 = -1
            dividend = -dividend
        if divisor < 0:
            key2 = -1
            divisor = -divisor
        key = key1 * key2

        if dividend < divisor:
            result =  0
        elif dividend == divisor:
            result =  1 * key
        elif abs(divisor) == 1:
            result =  key * dividend
        else:
            numb = 0
            while dividend > divisor:
                count = 1
                test_data = divisor

                while test_data < dividend:
                    if test_data + test_data < dividend:
                        test_data = test_data + test_data
                        count = count + count
                    else:
                        dividend = dividend - test_data
                        numb += count
            if dividend==divisor:
                numb+=1
            result =  numb * key

        if result>2147483647:
            return 2147483647
        elif result<-2147483648:
            return -2147483648
        else:
            return result