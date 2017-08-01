def set_answer(long_str):
    result_list = []
    int_numb = int(long_str)
    for i in range(10):
        result = i * int_numb
        result_list.append(result)
    return result_list


def add_up(list_of_str):
    result = 0
    for i in list_of_str:
        result = result + int(i)
    return str(result)


class Solution(object):
    def multiply(self, num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result_list = set_answer(num1)
        print(result_list)
        short_lenth = len(num2) - 1
        count = 0
        collect = []
        while short_lenth >= 0:
            index = int(num2[short_lenth])

            tem_result = str(result_list[index]) + '0' * count
            count += 1
            short_lenth -= 1
            collect.append(tem_result)
        result = add_up(collect)
        return result

        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
