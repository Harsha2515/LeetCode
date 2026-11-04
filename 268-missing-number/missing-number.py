class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = max(len(nums),max(nums))
        k = n*(n+1)/2
        return int(k - sum(nums))