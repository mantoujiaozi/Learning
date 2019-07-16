import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
#         myStack = []
#         node = root
#         seq = []

#         if node is None:
#             return True
        
#         while node or myStack:
#             while node:       
#                 myStack.append(node)
#                 node = node.left
            
#             node = myStack.pop()
#             seq.append(node.val)
#             node = node.right
        
#         print(seq)
#         length = len(seq[:math.floor(len(seq)/2)])
#         print(length)
#         lchild = seq[:math.floor(len(seq)/2)]
#         rchild = seq[math.floor(len(seq)/2)+1:]
#         print(lchild)
#         print(rchild)
#         if len(seq) % 2 == 0:
#             return False
#         for i in range(length):
#             if lchild[i] != rchild[length-i-1]:
#                 return False
            
#         return True
        def finder(lchild, rchild):
            if (lchild is None) and (rchild is None):
                return True
            if (lchild is None) or (rchild is None):
                return False
            

            a = finder(lchild.left, rchild.right)
            b = finder(lchild.right, rchild.left)
            
            if (lchild.val == rchild.val) and (a is True ) and (b is True):
                return True
            
            return False
        
        if root is None :
            return True
        return finder(root, root)




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True

        a = [root.left, root.right]
        while a:
            left = a.pop(0)
            right = a.pop(0)
            
            if (right is None) and (left is None):
                continue
            
            if (right is None) or (left is None):
                return False
                    
            
            if right.val != left.val:
                return False
            
            
            a.append(left.left)
            a.append(right.right)
            a.append(left.right)
            a.append(right.left)
            
           
        
        return True
    
