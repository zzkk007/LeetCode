"""
    203. 删除链表中等于给定值 val 的所有节点。

    示例:

    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""

# 超出时间限制
class Solution(object):
    def removeElements(self, head, val):

        if head is None:
            return None

        if head.val == val:
            return head.next

        pro = head
        node = head.next

        while node:
            if node.val == val:
                pro.next = node.next
            else:
                pro, node = node, node.next
        return head

"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # 链表不为空 并且 头节点值为 val 则 head = head.next.
        while head and head.val == val:
            head = head.next
        if not head:
            return head

        node = head.next
        pro = head

        while node:
            if node.val == val:
                pro.next = node.next
                node = node.next
            else:
                pro = node
                node = node.next
                # pro = pro.next
        return head



