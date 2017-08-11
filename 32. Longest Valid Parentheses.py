# the key point here is create a list to record the max_lenth at each point, and start with 1
# this is get the idea from pennlio in the discussion
# https://discuss.leetcode.com/topic/23559/pure-1d-dp-without-using-stack-python-with-detailed-explanation


class Solution(object):
    def longestValidParentheses(self, s):
        max_len_of_position = [0]*len(s)
        max_len_result = 0
        index = 1
        while index<len(s):
            if s[index] ==')':
                if s[index-1]=='(':
                    max_len_of_position[index] = max_len_of_position[index-2]+2
                elif index-max_len_of_position[index-1]-1>=0 and s[index-max_len_of_position[index-1]-1]=='(':
                    if max_len_of_position[index-1]>0:
                        max_len_of_position[index] = max_len_of_position[index - 1] + 2 + max_len_of_position[index-max_len_of_position[index-1]-2]
                    else:
                        max_len_of_position[index]=0
            max_len_result = max(max_len_result,max_len_of_position[index])
            index+=1
        print(max_len_of_position)
        return max_len_result