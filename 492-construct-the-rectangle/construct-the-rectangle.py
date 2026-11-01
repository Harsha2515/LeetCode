class Solution:
    import numpy as np
    def constructRectangle(self, area: int) -> list[int]:
        minDiff = -float('inf')
        result = []
        for W in range(1,int(area**0.5)+1):
            L = area//W
            diff = L - W
            minDiff = min(minDiff, diff)
            if minDiff != diff and L * W == area:
                result.append([L,W])
        return result[-1]