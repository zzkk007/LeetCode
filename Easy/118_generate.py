"""


    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。

    输入: 5
    输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]


"""


class Solution:
    def generate(self, num):
        if num < 1:
            return 0

        result = []

        for i in range(num-1):
            result.extend([])

