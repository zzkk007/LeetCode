

class Solution:
    def revoveDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        slowIndex = 0
        quickIndex = 1

        bound = len(nums)-1
        while quickIndex <= bound:
            if nums[slowIndex] != nums[quickIndex]:
                slowIndex += 1
                nums[slowIndex] = nums[quickIndex]

            quickIndex += 1

        print(nums)
        return slowIndex + 1


if __name__ == "__main__":

    s = Solution()
    alist = [0,0,1,1,1,2,2,2,3,3,4]
    print(s.revoveDuplicates(alist))

