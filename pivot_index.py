class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = 0

        if len(nums) == 1: return 0

        for i in range(1, len(nums)):
            right_sum += nums[i]

        if left_sum == right_sum:
            return 0

        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            # if i == len(nums) - 1:
            #     right_sum = 0
            if left_sum == right_sum:
                return i
        
        return -1