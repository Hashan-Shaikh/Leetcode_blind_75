class Solution(object):
    def uniqueOccurrences(self, arr):
        map = {}
        unique_values = set(arr)
        isUnique = True
        for num in arr:
            if num not in map:
                map[num] = 0
            map[num] += 1

        for value in unique_values:
            freq = map[value]
            for key in map:
                if key != value:
                    if map[key] == freq:
                        isUnique = False

        return isUnique
        
        
        