# first Solution is accpeted answer with comment
# second solution has problem in running time, but it's also work
# more beautiful thing of solution2 is, it's care about the  " ", could print out
# the result beautifully.



class Solution(object):
    def convert(self, s, numRows):
        if numRows ==1:
            return s
        if len(s)<= numRows:
            return s

        pattern_numb = numRows*2-2 # one repeated elemet number, not numRow, but a V shape
        result = ''
        for i in range(numRows):
            result = result+s[i]
            start_point = pattern_numb-i

                    # first line
            if i ==0:
                start_point = pattern_numb
            while i ==0 and start_point<len(s):
                result = result+ s[start_point]
                start_point = start_point+pattern_numb

                    # middle line
            while start_point<len(s) and i!=0 and i!=numRows-1:
                result = result+s[start_point]
                start_point = start_point+2*i
                if start_point<len(s):
                    result = result + s[start_point]
                start_point = start_point+2*(numRows-i-1)

                    # last line
            if i == numRows-1:
                start_point = i+pattern_numb
            while start_point<len(s) and (i == numRows-1):
                result = result+ s[start_point]
                start_point = start_point+pattern_numb

        return result






        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

wf = Solution()
print(wf.convert('PAYPALISHIRING',3))


def add_list(s,numb_of_row):
    # create a empty list
    list1 = []
    for i in range(numb_of_row):
        list1.append([])
    if len(s)<=numb_of_row:
        k = 0
        while k < len(s):
            list1[k].append(s[k])
            k+=1
        while k < numb_of_row:
            list1[k].append(' ')
            k += 1
        return list1
    else:
        #first filled the first column
        for i in range(numb_of_row):
            list1[i].append(s[i])
        s = s[numb_of_row:]
        col_numb = numb_of_row-2
        while col_numb>0 and len(s)>0:
                     #at least 1, which is the first empty
            first_empty = col_numb
            for i in range(first_empty):
                list1[i].append(' ')
            list1[first_empty].append(s[0])
            s = s[1:]
            while first_empty<numb_of_row-1: #first_empty from number to index
                list1[first_empty].append(' ')
                first_empty+=1
            col_numb = col_numb-1

        if len(s) ==0:
            return list1
        elif col_numb ==0:
            result2 = add_list(s,numb_of_row)
            for i in range(numb_of_row):
                list1[i] = list1[i]+ result2[i]
            return list1

def get_output(list1,numb_of_row):
    result = ''
    for i in range(numb_of_row):
        for k in list1[i]:
            if k !=' ':
                result = result+k
    return result

class Solution2(object):
    def convert(self, s, numRows):
        if numRows ==1:
            return s
        if len(s)<= numRows:
            return s
        result1 = add_list(s,numRows)
        result2 = get_output(result1,numRows)
        return result2

wf2 = Solution2()
print(wf2.convert('PAYPALISHIRING',3))
