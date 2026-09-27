class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def sumI(n):
            k = 0
            while n>0:
                k = k + n % 10
                n = n // 10
            return k
        
        for i in range(len(nums)):
            if i == sumI(nums[i]):
                return i
        return -1