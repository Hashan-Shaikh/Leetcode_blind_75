# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        
        depth = 1
        maxDepth = 0
        stack = [[root, depth]]
        while stack:
            prevDepth = depth
            node,depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return maxDepth
        