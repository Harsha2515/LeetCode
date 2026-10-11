class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumF = 0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                sumF += nums[i] * nums[i]
        return sumF