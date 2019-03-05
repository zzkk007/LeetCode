"""
    选择排序(Selection sort) 是一种简单直观的排序算法，
    工作原理就是：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕。

    时间复杂度

        最优时间复杂度：O(n2)
        最坏时间复杂度：O(n2)
        稳定性：不稳定（考虑升序每次选择最大的情况）

"""

def selection_Sort(alist):

    for i in  range(len(alist)-1):

        min_index = i

        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j

        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]

if __name__ == "__main__":

    alist = [9, 11, 32, 88, 3, 1, 34, 44, 2, 11, 49]
    print(alist)
    selection_Sort(alist)
    print(alist)