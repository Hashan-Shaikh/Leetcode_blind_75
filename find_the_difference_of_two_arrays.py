class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        sub_answer = []
        
        for num in set1:
            if num not in set2:
                sub_answer.append(num)

        answer.append(sub_answer)
        sub_answer = []

        for num in set2:
            if num not in set1:
                sub_answer.append(num)

        answer.append(sub_answer)
        return answer