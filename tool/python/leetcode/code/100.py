from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

#         if p is None and q is None:
#             return True
        
#         elif p and q and p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         else:
#             return False

        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            else:
                return False
        return True
