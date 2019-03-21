"""
    输入: [1, 2, 3, 4, 5, 6, 7]
    输出: {0:[3, 6],1:[1, 4, 7],2:[2, 5]}

def mod3(alist):

    hase_map = dict([(0,[]),(1,[]),(2,[])])

    for num in alist:
        hase_map[num%3].append(num)
    for k, v in hase_map.items():
        print(k,v)


    Python 字典(Dictionary) setdefault() 方法：
    描述：
        Python 字典 setdefault() 函数和 get() 方法类似，如果键不存在于字典中，
        将会添加键并将值设置为默认值。
    语法：
        dict.setdefault(key, default=None)

    参数：
        key - 查到的键值
        default - 键不存在，设置的默认值

    1、值为列表的构造方法：

        dic = {}
        dic.setdefault(key,[]).append(value)

        >>> dic = {}
        >>>
        >>> dic.setdefault('a',[]).append(1)
        >>> dic
        {'a': [1]}
        >>>
        >>> dic.setdefault('a',[]).append(2)
        >>> dic
        {'a': [1, 2]}
        >>> dic.setdefault('a',[]).append(4)
        >>> dic
        {'a': [1, 2, 4]}

    2、值为字典的构造方法：

        dic = {}
        dic.setdefault(key,{})[value] =1

        >>> dic = {}
        >>>
        >>> dic.setdefault('b',{})['f']=1
        >>> dic
        {'b': {'f': 1}}
        >>>
        >>> dic.setdefault('b',{})['g']=2
        >>> dic
        {'b': {'f': 1, 'g': 2}}
        >>>
        >>> dic.setdefault('b',{})['h']=3
        >>> dic
        {'b': {'f': 1, 'g': 2, 'h': 3}}
        >>>

"""

def mod3(alist):

    hase_map = dict()
    for num in alist:
        hase_map.setdefault(num%3,[]).append(num)

    for k, v in hase_map.items():
        print(k,v)


if __name__ == "__main__":
    mod3([1,2,3,4,5,6,7])