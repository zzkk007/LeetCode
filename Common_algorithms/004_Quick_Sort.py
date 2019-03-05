"""
    快速排序(Quick Sort), 又称分划交换排序，通过一次排序将要排序的数据分割成两个独立的部分，
    其中一部分的所有数据都比另外一部分数据小，然后再按照此方法对这两部分的数据分别进行快速排序，
    整个排序过程可以递归进行，依此达到整个数据变成有序数列。

    步骤为：

        1、从数列中提挑出一个元素，称为"基准"(Pivot)
        2、重新排列数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
          （相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。
           这个称为分区（partition）操作。

        3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

    时间复杂度

        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(n2)
        稳定性：不稳定

"""
def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


if __name__ == "__main__":

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)






