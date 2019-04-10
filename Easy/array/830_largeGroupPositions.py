"""
    830: 较大分组的位置

    在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。

    例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
    我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
    最终结果按照字典顺序输出。

    示例 1:

        输入: "abbxxxxzzy"
        输出: [[3,6]]
        解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。

    示例 2:

        输入: "abc"
        输出: []
        解释: "a","b" 和 "c" 均不是符合要求的较大分组。

    示例 3:

        输入: "abcdddeeeeaabbbcd"
        输出: [[3,5],[6,9],[12,14]]

    说明:  1 <= S.length <= 1000

"""
"""
题意：提取所有符合条件的子串的起始索引和结束索引

条件为：子串每个字符必须相等且连续三个以上

思路：将字符串转为字符数组，遍历整个数组，将符合条件的子串索引添加到List中。

如何筛选符合条件的子串：每次遍历，i代表当前遍历到的位置，开始索引beginIndex指向当前字符，
结束索引endIndex指向子串末尾索引，times表示出现重复字符的次数。如果符合条件，times自增，
当times大于3，就记录结束索引endIndex的值。上代码

class Solution(object):
    def largeGroupPositions(self, S):

        resList = list()
        i, beginIndex = 0, 0

        while i < len(S):

            beginIndex = i
            times = 0
            endIndex = -1

            while beginIndex < len(S) and S[i] ==  S[beginIndex]:
                beginIndex += 1
                times += 1
                if times >= 3:
                    endIndex = i + times - 1

            if endIndex == -1:
                i += 1
            else:
                resList.append([i, endIndex])
                i = endIndex

        return resList
"""

# 用双指针遍历，i为始指针，j为尾指针，外层为for循环，用于更新始指针i的值，
# 内层为while循环（连续的计数通常使用while循环），用于更新尾指针j的值，不断遍历后更新尾指针的值，
# 如果j-i>=3，就可以添加到list中了，然后在更新始指针i即可。

class Solution(object):
    def largeGroupPositions(self, S):
        lists = list()
        i = 0
        while i < len(S):
            j = i
            while j < len(S) and  S[i] == S[j]:
                j += 1
            if j - i >= 3:
                lists.append([i,j-1])
            i = j
        return lists







if __name__ == "__main__":

    S = Solution()
    #Str = "abcc"
    Str = "abcdddeeeeaabbbcd"
    print(S.largeGroupPositions(Str))

