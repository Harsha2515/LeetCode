class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        return sum(nums) - len(nums) * mini