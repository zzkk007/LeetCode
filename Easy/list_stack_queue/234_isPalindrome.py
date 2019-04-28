"""
    234. 回文链表

    请判断一个链表是否为回文链表。

    示例 1:

    输入: 1->2
    输出: false
    示例 2:

    输入: 1->2->2->1
    输出: true
    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]


# 时间复杂度O(n)， 空间复杂度O(1)

class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast = slow = head
        # 快指针指向下两个，这样遍历之后，slow只走到中间节点
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        # 将中间节点之后的链表反转
        p, rev = slow, None
        while p:
            rev, rev.next, p = p, rev, p.next

        # 重新以head开始比较反转后的链表
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True

