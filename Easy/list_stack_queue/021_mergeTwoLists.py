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

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = ListNode(None)
        node = res

        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return res.next


def LinkList(links):
    prev = ListNode(None)
    cur = prev
    for node in links:
        cur.next = node
        cur = cur.next
    return prev.next

def travel(links):

    cur = links
    while cur:
        print(cur.val)
        cur = cur.next

if __name__ == "__main__":

    links1 = []
    links1.append(ListNode(1))
    links1.append(ListNode(2))
    links1.append(ListNode(4))

    links2 = []
    links2.append(ListNode(1))
    links2.append(ListNode(3))
    links2.append(ListNode(4))

    l1 = LinkList(links1)
    travel(l1)

    l2 = LinkList(links2)
    travel(l2)
    print('--------------')

    S = Solution()
    l3 = S.mergeTwoLists(l1,l2)
    travel(l3)


