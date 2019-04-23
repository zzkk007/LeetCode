"""
    21. 合并两个有序链表

    将两个有序链表合并为一个新的有序链表并返回，
    新链表是通过拼接给定的两个链表的所有节点组成的。

    示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4


"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SignleLinkList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        cur = self.head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next
        print('')

    def add(self, item):
        node = ListNode(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        node = ListNode(item)
        if self.head == None:
            self.head = node

        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node


def mergeTwoLists(l1, l2):

    prev = None
    cur1 = l1.head
    cur2 = l2.head

    while cur1.next != None and cur2.next != None:
        if cur1.val <= cur2.val:
            prev = cur1
            cur1 = cur1.next
        else:
            prev = cur2
            cur2 = cur2.next








if __name__ == "__main__":

    l1 = SignleLinkList()
    l1.add(1)
    l1.append(2)
    l1.append(4)
    l1.travel()

    l2 = SignleLinkList()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    l2.travel()

    mergeTwoLists(l1,l2)
