class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxx = float('-inf')
        listt = []
        for candy in candies:
            if maxx < candy:
                maxx = candy

        for candy in candies:
            if candy + extraCandies >= maxx:
                listt.append(True)
            else:
                listt.append(False)

        return listt
        