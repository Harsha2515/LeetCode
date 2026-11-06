class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        leftMax = nums[0]
        currentMax = nums[0]
        partition = 0

        for i in range(1, len(nums)):
            currentMax = max(currentMax, nums[i])

            if nums[i] < leftMax:
                leftMax = currentMax
                partition = i

        return partition + 1