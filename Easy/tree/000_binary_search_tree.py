"""

    二叉搜索树： binary_search_tree

"""

from queue import Queue
import math

class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree(object):

    def __init__(self, val_list=[]):
        self.root = None

        for n in val_list:
            self.insert(n)

    def insert(self, data):
        """
        插入
        :param data:
        :return:
        """

        assert(isinstance(data, int))

        if self.root is None:
            self.root = TreeNode(data)
        else:
            n = self.root
            while n:
                p = n
                if data < n.val:
                    n = n.left
                else:
                    n = n.right
            new_node = TreeNode(data)
            new_node.parent = p

            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node

        return True

    def search(self, data):
        """
        搜索
        返回bst中所有值为 data 的节点列表
        :param data:
        :return:
        """
        assert(isinstance(data, int))

        # 所有搜索到的节点
        ret = []

        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    ret.append(n)
                n = n.right

        return ret

    def delete(self, data):
        """
        删除
        :param data:
        :return:
        """

        assert(isinstance(data, int))

        # 通过搜索得到需要删除的节点
        del_list = self.search(data)

        for n in del_list:
            # 父节点为空，又不是根节点，已经不再树上了，不用再删除
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node):
        """
        删除
        所有删除的节点N存在以下情况
        1. 删除节点没有子节点：直接删除 N 的父节点指针
        2. 有一个子节点：将 N 符节点指针指向 N 的子节点
        3. 有两个子节点：找到右子树的最小节点M, 将值赋值给N,然后删除 M
        :param node:
        :return:
        """

        # 1
        if node.left is None and node.right is None:
            # 情况 1 和 2，根节点和普通节点的处理方式不同

            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None

                # 将 node 指向父节点的指针指空。
                node.parent = None

        # 2
        elif node.left is None 

