class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set()
        set2 = set()
        answer = []
        sub_answer = []

        for num in nums1:
            set1.add(num)

        for num in nums2:
            set2.add(num)
        
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