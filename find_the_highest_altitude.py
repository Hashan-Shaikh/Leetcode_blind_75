class Solution(object):
    def largestAltitude(self, gain):
        maxx = float('-inf')
        gain.insert(0, 0)
        
        for i in range(2, len(gain)):
            gain[i] = gain[i] + gain[i-1]
        
        for element in gain:
            if maxx < element:
                maxx = element

        return maxx