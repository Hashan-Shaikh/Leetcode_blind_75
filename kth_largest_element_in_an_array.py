import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        k_th_largest = None
        for i in range(k):
            k_th_largest = -heapq.heappop(max_heap)

        return k_th_largest

        