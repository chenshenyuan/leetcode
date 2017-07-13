class Solution(object):
    def isValid(self, s):
        trigger_symbol = ['(', '{', '[']
        target_symbol = [')', '}', ']']
        result_list = []

        for i in range(len(s)):
            if s[i] in trigger_symbol:
                result_list.append(s[i])
            elif s[i] in target_symbol:
                index_numb = target_symbol.index(s[i])
                if len(result_list) == 0:
                    return False
                if result_list[-1] == trigger_symbol[index_numb]:
                    result_list.pop()
                else:
                    return False
            else:
                pass

        if len(result_list) == 0:
            return True
        else:
            return False