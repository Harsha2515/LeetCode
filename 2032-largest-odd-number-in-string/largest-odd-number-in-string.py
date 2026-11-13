class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums = num[::-1]
        reverse = ''
        for i in range(len(nums)):
            if int(nums[i]) % 2 != 0:
                reverse = nums[i:len(num)]
                break
        return reverse[::-1]