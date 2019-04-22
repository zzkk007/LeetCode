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
        elif node.left is None and node.right is not None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:

                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                node.parent = None
                node.right = None
        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None

        # 3
        else:

            min_node = node.right
            # 找到右子树的最小值节点

            if min_node.left:
                min_node = min_node.left

            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)

            #右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)

    def get_min(self):
        """
        返回最小值节点
        :return:
        """

        if self.root is None:
            return None

        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        """
        返回最大值
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.right:
            n = n.right
        return n.val

    def in_order(self):
        """
        中序遍历
        :return:
        """
        if self.root is None:
            return []

        return self._in_order(self.root)

    def _in_order(self, node):
        if node is None:
            return []

        ret = []
        n = node
        ret.extend(self._in_order(n.left))
        ret.append(n.val)
        ret.extend(self._in_order(n.right))

        return ret

    def __repr__(self):
        # return str(self.in_order())

        print(str(self.in_order()))
        return self._draw_tree()

    def _bfs(self):
        """
        bfs
        通过父子关系记录节点编号
        :return:
        """

        if self.root is None:
            return []

        ret = []
        q = Queue()
        #队列[节点，编号]
        q.put((self.root, 1))

        while not q.empty():
            n = q.get()

            if n[0] is not None:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1]*2))
                q.put((n[0].right, n[1]*2+1))

        return ret

    def _draw_tree(self):
        """
        可视化
        :return:
        """
        nodes = self._bfs()
        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1

        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str


if __name__ == "__main__":
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)

    print(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    for n in bst.search(2):
        print(n.parent.val, n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    # min max
    print(bst.get_max())
    print(bst.get_min())



