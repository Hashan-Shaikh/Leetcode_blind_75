class Solution(object):

    def greatestCommonDivisor(self, len1, len2):
        for i in range(min(len1, len2), 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                return i

    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        gcd = 0
        if str1 + str2 == str2 + str1:
            gcd = self.greatestCommonDivisor(len1, len2)
            return str1[:gcd]
        else:
            return ""