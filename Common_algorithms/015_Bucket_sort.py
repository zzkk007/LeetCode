"""

    假设我们现在需要对 D, a, F, B, c, A, z 这个字符串进行排序，
    要求将其中的所有小写字母都排在大写字母的前面，但小写字母内部和
    大写字母内部不要求有序，比如经过排序之后为 a, c, z, D, F, B, A
    这个该如何实现，如果字符串中存储不仅有大小写字母，
    还有数字，要将小写字母放到前面，不用排序算法，该怎么解决？


    利用桶排序思想，弄小写，大写，数字三个桶，遍历一遍，
    都放进去，然后再从桶中取出来就行了。相当于遍历了两遍，复杂度O(n)

"""

def bucket_sort(nums):
    low = list()
    upper = list()
    digit = list()
    for i in nums:
        if i.islower():
            low.append(i)
        elif i.isupper():
            upper.append(i)
        elif i.isdigit():
            digit.append(i)

    nums[:] = digit + low + upper

if __name__ == "__main__":

    nums = ['D', 'a', 'F', 'B', 'c', 'A', 'z', '1', 'd', '3', '4']
    print(nums)
    bucket_sort(nums)
    print(nums)

