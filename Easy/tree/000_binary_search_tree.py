"""
    二叉查找树又叫二叉搜索树。
    树中的任意一个节点，左子树上的每个节点都小于这个节点，
    而右子树上的每个节点都大于这个节点。

"""

class Node(object):
    """节点类"""
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
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue.pop(0)
            #print("treeNode:%d" % treeNode.elem)
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            elif treeNode.rchild == None:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)


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
        if root == None:
            return

        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)

            if node.lchild != None:
                queue.append(node.lchild)
            elif node.rchild != None:
                queue.append(node.rchild)

    def find(self, data):
        treeNode = self.root
        print(treeNode.elem)

        while treeNode:

            print(treeNode.elem)
            if data == treeNode.elem:
                return treeNode
            elif data < treeNode.elem:
                treeNode = treeNode.lchild
            elif data > treeNode.elem:
                treeNode = treeNode.rchild

        return None


if __name__ == "__main__":

    tree = Tree()
    tree.add(10)
    tree.add(8)
    tree.add(12)
    tree.add(6)
    tree.add(9)
    tree.add(11)
    tree.add(15)

    # tree.breadth_travel(tree.root)

    tree.preorder(tree.root)
    print('----------------')
    tree.inorder(tree.root)
    print('----------------')
    tree.postorder(tree.root)


    print('========start==========')


    #print(tree.find(1))