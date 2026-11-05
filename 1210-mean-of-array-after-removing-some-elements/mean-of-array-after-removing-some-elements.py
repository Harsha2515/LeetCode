class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n = len(arr)
        k = n // 20
        arr.sort()
        arr = arr[k:n-k]

        return sum(arr)/len(arr)