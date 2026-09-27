class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        Count = 0

        for i in nums:
            if i == 1:
                Count += 1
            else:
                Count = 0
            maxCount = max(maxCount, Count)
        return maxCount