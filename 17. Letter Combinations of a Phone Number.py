class Solution(object):
    def letterCombinations(self, digits):
        mapping = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result = []
        for i in range(len(digits)):
            if int(digits[i])<=1:
                return []
            else:
                numb_ind = int(digits[i])-2
                if len(result)==0:
                    for k in mapping[numb_ind]:
                        result.append(k)
                else:
                    temp_result = []
                    for k in result:
                        for w in mapping[numb_ind]:
                            temp_result.append(k+w)
                    result = temp_result
        return result