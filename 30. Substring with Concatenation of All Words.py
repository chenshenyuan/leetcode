class Solution(object):
    def findSubstring(self, s, words):
        words.sort()
        if len(s) == 0 or len(words) == 0:
            return []
        result = []
        ini_set = set()
        for word in words:
            ini_set.add(word[0])

        search_lenth = len(words) * len(words[0])
        word_lenth = len(words[0])
        index = 0
        while index <= len(s) - search_lenth:
            if s[index] not in ini_set:
                index += 1
            else:
                sub_str = s[index:index + search_lenth]
                test_words = [sub_str[i:i + word_lenth] for i in range(0, len(sub_str), word_lenth)]
                test_words.sort()

                if test_words == words:
                    result.append(index)
                index += 1
        return result

        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
