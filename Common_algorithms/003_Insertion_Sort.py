"""
    插入排序(Insertion Sort) 是一种简单直观的排序算法，

    它的工作原理是通过构建有序序列，对于未排序数据，在已排好
    序列中从后往前扫描，找到相应位置并插入，插入排序在实现上，
    在从后向前需要从后向前扫描过程中，需要反复的把已排序好的
    数据逐步向后挪位，为最新的元素提供插入空间。

    时间复杂度:

        最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
        最坏时间复杂度：O(n2)
        稳定性：稳定

"""

def insert_sort(alist):

    for i in range(1, len(alist)):
        for j in range(i,0,-1):
            if alist[j] < alist[j - 1]:
                alist[j],alist[j - 1] = alist[j - 1], alist[j]

if __name__ == "__main__":

    alist = [9, 3, 1, 33, 45, 22, 10, 0, 33, 87, 100]
    print(alist)
    insert_sort(alist)
    print(alist)