"""
    在一个二维数组中，每一行都按照从左到右递增的顺序排序， 每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数， 判断数组中是否含有该整数。

"""

arr = [[1,4,7,10,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]

def getNum(num, data = None):

    while data:
        if num > data[0][-1]:
            del data[0]
            getNum(num, data)

        elif num < data[0][-1]:

            data = list(zip(*data))
            del data[-1]
            data = list(zip(*data))
            print(data)
            getNum(num, data = None)

        else:
            return True

    return False

if __name__ == '__main__':
    print(getNum(16, arr))