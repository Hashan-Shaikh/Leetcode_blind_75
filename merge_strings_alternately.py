class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        i = 0
        if len(word2) == 0:
            return word1
        
        maxx = max(len(word1), len(word2))

        while i < maxx:
            if i == len(word1):
                res += word2[i:]
                break
            elif i == len(word2):
                res += word1[i:]
                break
            res = res + word1[i] + word2[i]
            i += 1

        return res
        