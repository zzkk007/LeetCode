"""
    014 : 计数排序：

        计数排序其实是桶排序的一种特殊情况。当要排序的 n 个数据，所处的范围并不大的时候，
        比如最大值是 k，我们可以把数据划分成 k 个桶。每个桶里面的数值都是相同的，省掉了
        桶内排序的时间。

        计数排序的算法思想就是这么简单，更桶排序非常类似，只是桶的大小粒度不一样。不过，
        为什么这个排序算法叫“计数”排序呢？“计数”的含义来自哪里呢？

        想弄明白这个问题，我们就要来看计数排序算法的实现方法。
        假设只有 8 个考生，分数在 0 到 5 分之间。这 8 个考生的成绩我们放在一个数组 A[8]中
        他们分别是：2，5，3，0，2，3，0，3。

        考生的成绩从 0 到 5 分，我们使用大小为 6 的数组 C[6] 表示桶，其中下标对应分数，C[6]
        内存储的并不是考生，而是对应的考生个数。我们只需要遍历一遍考生分数，就可以得到 C[6]的值。

            C[6]  2  0  2  3  0  1  内容--个数
                  0  1  2  3  4  5  下标--分数

        从图中可以看出，分数为 3 分的考生有 3 个，小于 3 分的考生有 4 个，所以，成绩为 3 分的
        考生在排序之后的有序数组 R[8] 中，会保存下标 4，5，6 的位置。

            R[8]  0  0  2  2  3  3  3  5
                  0  1  2  3  4  5  6  7

        那么我们如何快速计算出，每个分数的考生在有序数据中的存储位置呢？
        这个处理方法非常巧妙，很不容易想到。

        思路是这样的：我们对 C[6] 数据顺序求和，C[6]存储的数据就变成了下面这样子。
        C[k]里存储小于等于分数 K 的考生个数。

            C[6] 2  2  4  7  7  8
                 0  1  2  3  4  5

        我们从后到前依次扫描数组 A[2，5，3，0，2，3，0，3], 比如，当扫描到 3 时
        我们可以从数组 C 中取出下标为 3 的值 7，也就是说，到目前为止，包括自己在内
        分数小于等于3 的考生有7个，也就是说 3 是数组 R 中的第 7 个元素(也就是数组R
        中下标为 6 的位置)，当把 3 从A数组中取出放入到数组R中后，小于等于 3 的元素
        就只剩下了 6 个了，所以相应的 C[3] 要减 1， 变成 6。

        依次类推，当我们扫描到第 2 个分数为 3 的考生的时候，就会把它放入数组R中第6个元素
        的位置(也就是下标为 5 的位置)。当我们扫描完整个数组 A 后，数组 R 内的数据就是按照
        分数从小到大有序排序的了。

        这种利用另外一个数组来计数的实现排序算法的方式叫做计数排序，
        计数排序只能用在数据范围不大的场景中，如果数据范围 k 要比排序
        的数据 n 大很多，就不适合计算排序了，如果要排序的数据是其他类型的
        要将其在不改变相对大小的情况下，转换为非负整数。


from typing import List
import itertools

def counting_sort(a: List[int]):
    if len(a) <= 1: return

    # a中有counts[i]个数不大于i
    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))

    # 临时数组，储存排序之后的结果
    a_sorted = [0] * len(a)
    for num in reversed(a):
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1

a[:] = a_sorted


"""

# 计数排序，a 是数组，n 是数组大小，
# 假设数组中存储都是非负整数。


def countingSort(a, n):

    if n <= 1:
        return

    # 查找数组中数据的范围
    max = a[0]
    for i in range(1, n):
        if(max < a[i]):
            max = a[i]

    # 申请一个计数数组 c, 下标大小为[0, max]
    c = [0]*(max + 1)
    # print(c)
    # print('---------------------')

    # 计算每个元素的个数，放入 c 中
    for i in range(n):
        c[a[i]] += 1
    # print(c)
    # print('---------------------')


    # 依次累加
    for i in range(1, max + 1):
        c[i] = c[i - 1] + c[i]
    # print(c)
    # print('---------------------')

    # 临时数组 r, 存储排序之后的结果
    r = [None]*n

    for i in range(n-1, -1, -1):
        index = c[a[i]] - 1
        r[index] = a[i]
        c[a[i]] -= 1
    # print(r)

    # 将结果拷贝给 a 数组
    # for i  in range(n):
    #    a[i]= r[i]
    a[:] = r


if __name__ == "__main__":

    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    print(nums)
    countingSort(nums, len(nums))
    print(nums)
