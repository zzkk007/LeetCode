"""
    一个数组，去掉重复的值，顺序不变，数组中的值不仅仅只有整数。

"""
def repeat_an_array(alist):

    for i in range(len(alist)-1):
        for j in range(i+1, len(alist)):
            if alist[i] == alist[j]:
                pass


if __name__ == "__main__":


    alist = [1, '22', (1,'2'), {1:'1'}, '22', 3, 4, 1]
    print(alist)
    repeat_an_array(alist)
    print(alist)
