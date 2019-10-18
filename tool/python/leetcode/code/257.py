# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        path = ''
        if root == None:
            return self.ans
        if root:
            path += str(root.val)
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans.append(path)
            if root.left:
                root.left = dfs(root.left, path + '->' + str(root.left.val))
            if root.right:
                root.right = dfs(root.right, path + '->' + str(root.right.val))

        dfs(root, path)
        return self.ans
