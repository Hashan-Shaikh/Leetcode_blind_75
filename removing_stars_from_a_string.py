from collections import deque
class Solution(object):
    def removeStars(self, s):
        res = ""
        stack = deque()
        
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
        