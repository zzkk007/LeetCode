"""
    237. 删除链表中的节点.

    说明:
        链表至少包含两个节点。
        链表中所有节点的值都是唯一的。
        给定的节点为非末尾节点并且一定是链表中的一个有效节点。
        不要从你的函数中返回任何结果。

    方法：与下一个节点交换
    从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点。

    因为我们无法访问我们想要删除的节点之前的节点，我们始终不能修改该节点的 next 指针。
    相反，我们必须将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。




"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next