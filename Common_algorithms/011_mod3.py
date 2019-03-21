"""
    输入: [1, 2, 3, 4, 5, 6, 7]
    输出: {0:[3, 6],1:[1, 4, 7],2:[2, 5]}

"""

def mod3(alist):

    hase_map = dict([(0,[]),(1,[]),(2,[])])

    for num in alist:
        hase_map[num%3].append(num)
    for k, v in hase_map.items():
        print(k,v)



if __name__ == "__main__":
    mod3([1,2,3,4,5,6,7])