

class Solution:
    def revoveDuplicates(self, nums):

        temp_list = []
        for key,num in enumerate(nums):
            if num not in temp_list:
                temp_list.append(num)

        print(temp_list)
        return len(temp_list)



if __name__ == "__main__":

    s = Solution()
    alist = [1,1,2]
    print(s.revoveDuplicates(alist))

