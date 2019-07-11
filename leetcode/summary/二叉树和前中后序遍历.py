# *_*coding:utf-8 *_*

class BinNode():
    def __init__(self, lchild=None, rchild=None, val=0):
        self.lchild = lchild
        self.rchild = rchild
        self.val = val

class BTree():
    def __init__(self, base=0):
        self.base = base

    def preOrder(self, root):

        if root is None:
            return

        myStack = []
        node = root
        seq = []  # 记录先序访问序列
        while node or myStack:
            while node:
                seq.append(node.val)
                myStack.append(node)
                node = node.lchild

            node = myStack.pop()
            node = node.rchild

        return seq

    def inOrder(self, root):

        if root is None:
            return

        myStack = []
        seq = []  # 记录先序访问序列
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild

            node = myStack.pop()
            seq.append(node.val)
            node = node.rchild

        return seq

    def later_stack(self, root):
        if root is None:
            return
        myStack1 = []
        myStack2 = []
        seq = []
        node = root
        myStack1.append(node)
        while myStack1:
            # 找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            # 将myStack2中的元素出栈，即为后序遍历次序
            seq.append(myStack2.pop().val)
        return seq


tree1 = BinNode(val=8)
tree2 = BinNode(val=9)
tree3 = BinNode(tree1, val=6)
tree4 = BinNode(tree2, 0, val=7)
base = BinNode(tree3, tree4, 5)
# print(base.lchild.lchild.val)
btree = BTree(base)
# btree.later_stack(btree.base)
print(btree.later_stack(btree.base))