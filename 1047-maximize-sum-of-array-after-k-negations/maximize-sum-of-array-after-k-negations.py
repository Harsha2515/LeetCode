class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        for i in range(k):
            nums[nums.index(min(nums))] *= -1
        return sum(nums)