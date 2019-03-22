"""
    一个数组，去掉重复的值，顺序不变，数组中的值不仅仅只有整数。

"""
def repeat_an_array(alist):

    #hase_map = dict()
    result = []

    #for k, v in enumerate(alist):
    #    hase_map[k] = v

    for vaule in alist:
        if vaule in result:
            continue
        else:
            result.append(vaule)
    return result

if __name__ == "__main__":


    alist = [1, '22', (1,'2'), {1:'1'}, '22', 3, 4, 1, {1:'1'}, (1,'2'), '5']
    print(alist)
    result = repeat_an_array(alist)
    print(result)
