# https://discuss.leetcode.com/topic/28240/9-lines-of-python-code
# no idea of path.


class Solution(object):
    def simplifyPath(self, path):
        places = [p for p in path.split("/") if p != "." and p != ""]
        print(places)
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

        """
        :type path: str
        :rtype: str
        """