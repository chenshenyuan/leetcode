def generator(left_list):
    mapp_list = ['(', ')']
    result = []
    if left_list[0] > 1 and left_list[1] > 1:
        if left_list[0] == left_list[1]:
            temp_result = generator([left_list[0] - 1, left_list[1]])
            for i in temp_result:
                result.append(mapp_list[0] + i)
        elif left_list[0] < left_list[1]:
            temp_result = generator([left_list[0] - 1, left_list[1]])
            for i in temp_result:
                result.append(mapp_list[0] + i)
            temp_result = generator([left_list[0], left_list[1] - 1])
            for i in temp_result:
                result.append(mapp_list[1] + i)

    elif left_list[0] == 1 and left_list[1] > 1:
        loc = 0
        while loc < left_list[1]:
            temp_result = ''
            for i in range(left_list[1] + 1):
                if loc == i:
                    temp_result = temp_result + mapp_list[0]
                else:
                    temp_result = temp_result + mapp_list[1]
            result.append(temp_result)
            loc += 1
    else:
        temp_result = mapp_list[0] + mapp_list[1]
        result.append(temp_result)
    return result


class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []

        left_list = [n, n]
        result = generator(left_list)
        return result
        """
        :type n: int
        :rtype: List[str]
        """
