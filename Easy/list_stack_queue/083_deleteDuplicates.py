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

# 这是一个简单的问题，仅测试你操作列表的结点指针的能力。
# 由于输入的列表已排序，因此我们可以通过将结点的值与它之后的结点进行比较来确定它是否为重复结点。
# 如果它是重复的，我们更改当前结点的 next 指针，以便它跳过下一个结点并直接指向下一个结点之后的结点。

class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
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



