# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
#         def finder(root,lower = float('-inf'), upper = float('inf')):
            
#             if (root is None ):
#                 return True
            
            
#             if (root.val >= upper) or (root.val <= lower):
#                 return False
            

#             if not finder(root.left, lower, root.val):
                
#                 return False
            
#             if not finder(root.right, root.val, upper):
                
#                 return False
            
#             return True
        
#         return finder(root)

        stack = []
        seq = float('-inf')

        node = root
        while node or (len(stack) !=0):
            
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            if node.val <= seq:
                return False
            
            seq = node.val
            node = node.right
            
        return True