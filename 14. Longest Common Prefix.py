def find_shortest(list_input):
    shortest = list_input[0]

    for i in range(1, len(list_input)):
        if len(list_input[i]) < len(shortest):
            shortest = list_input[i]
    return shortest


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return find_shortest(strs)

        shortest_str = find_shortest(strs)

        count = 0

        while len(shortest_str) >= 1:
            str_len = len(shortest_str)
            for i in strs:

                if shortest_str == i[:str_len]:
                    count += 1
                else:
                    break

            if count == len(strs):
                return shortest_str
            else:
                count = 0
                shortest_str = shortest_str[:-1]
        return shortest_str
        """
        :type strs: List[str]
        :rtype: str
        """
