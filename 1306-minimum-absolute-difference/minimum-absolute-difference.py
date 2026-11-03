class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minDiff = float('inf')
        result = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]

            if diff < minDiff:
                minDiff = diff
                result = [[arr[i-1], arr[i]]]

            elif diff == minDiff:
                result.append([arr[i-1], arr[i]])

        return result