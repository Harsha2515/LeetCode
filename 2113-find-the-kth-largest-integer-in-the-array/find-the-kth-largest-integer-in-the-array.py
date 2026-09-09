class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if len(nums)<k:
            return None

        arr = []

        for i in nums:
            arr.append(int(i))
        arr.sort()
        return str(arr[-k])
