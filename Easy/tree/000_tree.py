"""
    用数组存储法创建一个二叉树，并进行遍历

"""

class Node(object):
    """节点类"""
    def __init__(self, elem = None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
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


if __name__ == "__main__":

    tree = Tree()
    tree.add(10)
    tree.add(8)
    tree.add(12)
    tree.add(6)
    tree.add(9)
    tree.add(11)
    tree.add(15)
    #tree.preorder(tree.root)
    tree.breadth_travel(tree.root)
    #tree.inorder(tree.root)
    #tree.postorder(tree.root)




