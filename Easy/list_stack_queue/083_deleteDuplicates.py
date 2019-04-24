"""
    83. 删除排序链表中的重复元素

    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

    示例 1:

        输入: 1->1->2
        输出: 1->2

    示例 2:

        输入: 1->1->2->3->3
        输出: 1->2->3

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            temp = cur
            while temp.next:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            cur = cur.next
        return head

if __name__ == "__main__":

    links1 = []
    links1.append(ListNode(1))
    links1.append(ListNode(1))
    links1.append(ListNode(2))

    l1 = LinkList(links1)
    travel(l1)
    print('-----------------')

    S = Solution()
    l2 = S.deleteDuplicates(l1)
    travel(l2)



