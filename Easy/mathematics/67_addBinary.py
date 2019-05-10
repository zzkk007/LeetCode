
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        return bin(int(a,2) + int(b, 2)).replace('0b','')





if __name__ == "__main__":

    S = Solution()
    print(S.addBinary("111", '111'))