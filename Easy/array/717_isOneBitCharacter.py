"""
    717: 1比特与2比特字符

    有两种特殊的字符。第一种字符可以用一比特 0 来表示。
    第二种字符可以用两比特(10或11)来表示。

    现给一个由若干比特组成的字符串，问最后一个字符串是
    否必定为一个比特字符。给定的字符串总是由 0 结束。

    示例1：

        输入： bits = [1, 0, 0]
        输出：True
        解释：唯一的编码方式是一个两个比特字符和一个比特字符。
             所以最后一个字符是一比特字符。

    示例2：

        输入：bits = [1, 1, 1, 0]
        输出：False
        解释：唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

    注意：

        1 <= len(bits) <= 1000.
        bits[i] 总是0 或 1.

"""

"""
# 只与最后一个元素0的前面的连续1的个数有关系。

class Solution(object):
    def isOneBitCharacter(self, bits):
        count = 0
        for i in range(len(bits)-2, -1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        
        if count % 2 == 0:
            return True
        return False

"""

# 遇到 1 索引+2，遇到 0 索引+1，最后比较索引与列表长度即可
class Solution(object):
    def isOneBitCharacter(self, bits):

        i = 0
        while (i<len(bits)-1):
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i >= len(bits):
            return False
        else:
            return True

if __name__ == "__main__":

    S = Solution()
    bits = [1, 0, 0, 0]
    print(S.isOneBitCharacter(bits))




