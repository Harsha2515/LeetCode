class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = max(nums)
        moves = 0
        for i in nums:
            moves += n-i
        return moves