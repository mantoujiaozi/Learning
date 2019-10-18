"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # def finder(root, depth):
        if root is None:
            return 0
        if root.children is None:
            return 1
        depth = 1
        for i in root.children :
            depth_t = self.maxDepth(i) + 1
            
            if depth_t > depth:
                depth = depth_t         
        
        return depth
            