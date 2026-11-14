class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        SumNum = []
        for p in range(l,r+1):
            i = 0
            j = p + i
            while(j<=len(nums)):
                if sum(nums[i:j]) > 0:
                    SumNum.append(sum(nums[i:j]))
                i += 1
                j += 1
            
        if SumNum:
            return min(SumNum)
        else:
            return -1