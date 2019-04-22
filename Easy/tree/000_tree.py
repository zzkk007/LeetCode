"""
    用数组存储法创建一个二叉树，并进行遍历

class Node(object):
    def __init__(self, elem = None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):

    def __init__(self, root=None):
        self.root = root
        self.myQueue = []

    def add(self, elem):

        node = Node(elem)
        if self.root is None:
            self.root = node
            self.myQueue.append(node)

        else:
            treeNode = self.myQueue.pop(0)
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                #self.myQueue.pop(0)
"""


class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):

        # 前序遍历，根、左、右
        if root == None:
            return

        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self,root):

        # 中序遍历，左、根、右
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        # 后序遍历， 左、右、根
        if root == None:
            return

        self.preorder(root.lchild)
        self.preorder(root.rchild)
        print(root.elem)


    def breadth_travel(self, root):
        # 广度优先遍历(层次遍历)
        # 利用队列实现的层次遍历

        if root == None:
            return

        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


    def pre_order(self, root):
        if root:
            yield root.elem
            yield from self.pre_order(root.lchild)
            yield from self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            yield from self.in_order(root.lchild)
            yield root.elem
            yield from self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            yield from self.post_order(root.lchild)
            yield from self.post_order(root.rchild)
            yield root.elem

if __name__ == "__main__":

    tree = Tree()
    tree.add(10)
    tree.add(8)
    tree.add(12)
    tree.add(6)
    tree.add(9)
    tree.add(11)
    tree.add(15)
    # tree.preorder(tree.root)
    # tree.breadth_travel(tree.root)
    # tree.inorder(tree.root)
    # tree.postorder(tree.root)

    # print(list(tree.pre_order(tree.root)))
    # print(list(tree.in_order(tree.root)))
    print(list(tree.post_order(tree.root)))

